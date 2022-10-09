from os.path import dirname, basename, isfile, join
import glob


class Package:
    def __init__(self, file_path):
        self.file_path = file_path

    def import_all_modules(self):
        app_name = self.file_path.split('\\')[-3]
        package_name = self.file_path.split('\\')[-2]
        module_names = self.get_module_names()

        for module_name in module_names:
            __import__(app_name + '.' + package_name + '.' + module_name)

    def get_module_names(self):
        module_paths = glob.glob(join(dirname(self.file_path), "*.py"))
        module_names = [basename(f)[:-3] for f in module_paths if isfile(f) and not f.endswith('__init__.py')]
        return module_names
