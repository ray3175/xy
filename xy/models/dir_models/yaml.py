import os
import asyncio
from concurrent.futures import ThreadPoolExecutor
from ...stdlib_overwrite.dict import Dict
from ..file_models.yaml import YamlModel
from . import DirModel


class YamlDirModel(DirModel):
    def __init__(self, dir_path, removesuffix=True):
        super().__init__(dir_path, file_regex=".*\.yaml")
        self.__data = asyncio.run(self.__init_yaml_dir_data(self.data, removesuffix, ThreadPoolExecutor(max_workers=os.cpu_count(), thread_name_prefix="xy.models.dir_models.yaml.YamlDirModel")))

    async def __new_yaml_model(self, yaml_path, executor):
        return await asyncio.get_event_loop().run_in_executor(executor, YamlModel, yaml_path)

    async def __init_yaml_dir_data(self, super_data, removesuffix, executor):
        data = Dict()
        for key, value in super_data.items():
            if isinstance(value, dict):
                data[key] = asyncio.create_task(self.__init_yaml_dir_data(value, removesuffix, executor))
            else:
                data[key.removesuffix(".yaml") if removesuffix else key] = asyncio.create_task(self.__new_yaml_model(value, executor))
        for key, value in data.items():
            data[key] = await value
        return data

    def get_data(self):
        return self.__data

