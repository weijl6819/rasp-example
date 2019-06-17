import sys
import imp
class _InstallFcnHook(object):
    def __init__(self, fcn):
        self._fcn = fcn
    
    def _pre_hook(self, *args, **kwargs):
        print("wtf")
        return (args, kwargs)

    def __call__(self, *args, **kwargs):
        (_hook_args, _hook_kwargs) = self._pre_hook(*args, **kwargs)
        retval = self._fcn(*_hook_args, *_hook_kwargs)
        return retval

fd, pathname, desc = imp.find_module(__name__, sys.path[::-1])
mod = imp.load_module(__name__, fd, pathname, desc)


system = _InstallFcnHook(system)
