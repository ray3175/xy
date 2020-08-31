from ..stdlib_overwrite.dict import Dict
from ..decorator.singleton import Singleton


@Singleton
class GlobalData(Dict):
    pass

