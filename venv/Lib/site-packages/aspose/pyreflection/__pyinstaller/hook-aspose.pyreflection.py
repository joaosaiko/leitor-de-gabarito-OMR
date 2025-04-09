from PyInstaller.utils.hooks import get_package_paths
import os.path

(_, root) = get_package_paths('aspose')

datas = [(os.path.join(root, 'assemblies', 'pyreflection'), os.path.join('aspose', 'assemblies', 'pyreflection'))]

hiddenimports = [ 'aspose', 'aspose.pygc' ]

