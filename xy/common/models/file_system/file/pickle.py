import pickle
import aiofiles
from . import FileModel


class PickleModel(FileModel):
    def __init__(self, pickle_path, read_content=False, read_data=False):
        super(PickleModel, self).__init__(pickle_path, read_content, read_data)

    def read_data(self, *args, **kwargs):
        with open(self.path, "rb") as _pickle:
            self.data = pickle.load(_pickle)
        return self.data

    def write_data(self, *args, **kwargs):
        with open(self.path, "wb") as _pickle:
            pickle.dump(self.data, _pickle)
        return self.data

    async def async_read_data(self, *args, **kwargs):
        async with aiofiles.open(self.path, "rb") as _pickle:
            self.data = pickle.loads(await _pickle.read())
        return self.data

    async def async_write_data(self, *args, **kwargs):
        async with aiofiles.open(self.path, "wb") as _pickle:
            await _pickle.write(pickle.dumps(self.data))
        return self.data

