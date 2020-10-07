from ...stdlib_overwrite.dict import Dict
from ..file_models.yaml import YamlModel
from . import DirModel


class YamlDirModel(DirModel):
    def __init__(self, dir_path, removesuffix=True):
        super().__init__(dir_path, file_regex=".*\.yaml")
        self.__data = self.__init_yaml_dir_data(self.data, removesuffix)

    def __init_yaml_dir_data(self, super_data, removesuffix=True):
        data = Dict()
        for key, value in super_data.items():
            if isinstance(value, dict):
                data[key] = self.__init_yaml_dir_data(value)
            else:
                data[key.removesuffix(".yaml") if removesuffix else key] = YamlModel(value)
        return data

    def get_data(self):
        return self.__data

