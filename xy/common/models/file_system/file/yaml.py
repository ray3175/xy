import yaml     # pip install pyyaml
from ruamel import yaml as ryaml
from . import FileModel


class YamlModel(FileModel):
    def __init__(self, yaml_path, read_content=False, read_data=False, code_type="utf-8"):
        super().__init__(yaml_path, read_content, read_data, code_type)

    def read_data(self, code_type="utf-8") -> (list, dict, None):
        data = super().read_data()
        try:
            self.data = yaml.load(data, Loader=yaml.FullLoader)
        except yaml.composer.ComposerError:
            self.data = list(yaml.load_all(data, Loader=yaml.FullLoader))
        return self.data

    def write_data(self, code_type="utf-8") -> (list, dict, None):
        with open(self.path, "w", encoding=code_type) as _yaml:
            if isinstance(self.data, list):
                ryaml.dump_all(self.data, _yaml, Dumper=ryaml.RoundTripDumper)
            else:
                ryaml.dump(self.data, _yaml, Dumper=ryaml.RoundTripDumper)
            _yaml.close()
        return self.data

