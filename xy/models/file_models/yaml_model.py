import yaml     # pip install pyyaml
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
            self.data = yaml.load(self.data, Loader=yaml.FullLoader)
        except yaml.composer.ComposerError:
            self.data = yaml.load_all(self.data, Loader=yaml.FullLoader)

    def get_data(self):
        return self.data

