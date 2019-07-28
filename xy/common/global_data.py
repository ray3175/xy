from ..decorator.singleton import Singleton
from ..arith.dict.ray_dict import RayDict


@Singleton
class GlobalData(RayDict):
    pass
