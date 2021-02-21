import pickle
from . import FileModel


class PickleModel(FileModel):
    def __init__(self, pickle_path, read_content=False, read_data=False):
        super(PickleModel, self).__init__(pickle_path, read_content, read_data)

    def read_data(self, *args, **kwargs):
        with open(self.path, "rb") as _pickle:
            self.data = pickle.load(_pickle)
            _pickle.close()
        return self.data

    def write_data(self, *args, **kwargs):
        with open(self.path, "wb") as _pickle:
            pickle.dump(self.data, _pickle)
            _pickle.close()
        return self.data

