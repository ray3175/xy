from ...stdlib_overwrite.dict import Dict
from .is_pd import IsPd


class Tables(Dict):
    def save_table(self, name, pd):
        _return = None
        if IsPd.is_pd(pd):
            self.update({name: pd})
            _return = True
        return _return
