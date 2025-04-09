import os
import sys
import re
import glob
import platform
from importlib import import_module
import importlib.abc as impabc 
import importlib.machinery as impmach
from types import ModuleType

_pkg_dir = os.path.dirname(__file__)

os.environ['NETCORE_WRAPPER_NETCORE_DIR_aspose'] = os.path.join(_pkg_dir, 'netcore')
    
os.environ['NETCORE_WRAPPER_ASSEMBLY_DIR_aspose'] = os.path.join(_pkg_dir, 'assemblies')
    
os.environ['WRAPPER_MODULE_DIR_aspose'] = _pkg_dir

__path__ = []

def get_vspec_ext_suffixes():    
    ver_maj_min = ''.join(str(x) for x in sys.version_info[:2])
    return [sfx for sfx in impmach.EXTENSION_SUFFIXES if ver_maj_min in sfx]

_vspec_ext_suffixes = get_vspec_ext_suffixes()

def get_all():
    is_win_not_debug = (platform.system() == 'Windows') and (next((sfx for sfx in _vspec_ext_suffixes if sfx.startswith('_d')), None) is None) 
    all_dict = dict()
    for entry in glob.glob(os.path.join(_pkg_dir, '*')):
        if os.path.isfile(entry):
            _,filename = os.path.split(entry)
            mod_name = next((filename[:-len(sfx)] for sfx in _vspec_ext_suffixes if filename.endswith(sfx)), None)
            if not ((mod_name is None) or ('.' in mod_name) or (is_win_not_debug and mod_name.endswith('_d'))):
                all_dict[mod_name] = mod_name
    return list(all_dict.keys())

__all__ = get_all()

if sys.version_info < (3, 6, 0):
    def imp_error_t(cls):
        cls._imp_error_t = ImportError
        return cls
else:
    def imp_error_t(cls):
        cls._imp_error_t = ModuleNotFoundError
        return cls

@imp_error_t
class AsposeSubModuleLoader(impabc.Loader):
    def create_module(self, spec):
        package_name,_,module_name = spec.name.rpartition('.')
        package_obj = import_module(package_name)
        module_obj = getattr(package_obj, module_name, None)
        if module_obj is None:
            err = self._imp_error_t('No module named \''+spec.name+'\'; module \''+package_name+'\' has no submodule \''+module_name+'\'')
            raise err
        if not isinstance(module_obj, ModuleType):
            err = self._imp_error_t('No module named \''+spec.name+'\'; \''+spec.name+'\' is not a module')
            raise err
        return module_obj
    def exec_module(self, module):
        pass

class AsposeMetaPathFinder(impabc.MetaPathFinder):
    _chk_re = re.compile(__package__+r'\.([^.]+)(\.)?')
    _submod_loader = AsposeSubModuleLoader()

    def find_spec(self, fullname, path, target=None):
        m = self._chk_re.match(fullname)
        if not (m is None):
            if m.group(2) is None:
               module_name = m.group(1)
               for sfx in _vspec_ext_suffixes:
                   filename=os.path.join(_pkg_dir, module_name+sfx)
                   if os.path.isfile(filename):
                       return impmach.ModuleSpec(fullname, impmach.ExtensionFileLoader(fullname, filename), origin=filename, is_package=True)
            else:
               return impmach.ModuleSpec(fullname, self._submod_loader, is_package=True)
        pass

sys.meta_path.append(AsposeMetaPathFinder())
