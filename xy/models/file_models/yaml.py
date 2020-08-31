import yaml     # pip install pyyaml
from ...stdlib_overwrite.list import List
from ...stdlib_overwrite.dict import Dict
from . import FileModel


class YamlModel(FileModel):
    def __init__(self, yaml_path):
        super().__init__(yaml_path)
        self.__init_data()

    @property
    def path(self):
        return self.get_path()

    @path.setter
    def path(self, path):
        self.set_path(path)

    @path.deleter
    def path(self):
        self.set_path(None)

    def __init_data(self):
        try:
            self.data = Dict(_dict) if (_dict:=yaml.load(self.data, Loader=yaml.FullLoader)) else _dict
        except yaml.composer.ComposerError:
            self.data = List([Dict(_dict) for _dict in yaml.load_all(self.data, Loader=yaml.FullLoader) if _dict])

    def get_data(self):
        return self.data





