from ..decorator.singleton import Singleton
from xy.arith.dict.ray_dict import RayDict


@Singleton
class GlobalData(RayDict):
    pass
