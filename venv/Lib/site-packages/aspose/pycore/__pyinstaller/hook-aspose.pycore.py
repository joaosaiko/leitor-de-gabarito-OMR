from PyInstaller.utils.hooks import get_package_paths
import os.path

(_, root) = get_package_paths('aspose')

datas = [(os.path.join(root, 'assemblies', 'pycore'), os.path.join('aspose', 'assemblies', 'pycore'))]

datas += [(os.path.join(root, 'pycore'), os.path.join('aspose', 'pycore'))]

hiddenimports = [ 'aspose', 'aspose.pygc' ]

