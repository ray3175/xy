from ..decorator.singleton import Singleton
from ..arith.ray_dict import RayDict


@Singleton
class GlobalData(RayDict):
    pass
