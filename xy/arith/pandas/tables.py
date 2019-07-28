from .is_pd import IsPd
from ..dict.ray_dict import RayDict
from ...decorator.singleton import Singleton


@Singleton
class Tables(RayDict):
    def save_table(self, name, pd):
        _return = None
        if IsPd.is_pd(pd):
            self.update({name: pd})
            _return = True
        return _return
