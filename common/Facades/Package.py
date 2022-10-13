from os.path import dirname, basename, isfile, join
import glob
import os


class Package:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def import_all_modules(self):
        """
        Import all modules in a package of first level from
        the Django app that has been used.
        """
        folders = os.path.normpath(self.file_path).split(os.sep)
        app_name = folders[-3]
        package_name = folders[-2]
        module_names = self.get_module_names()

        for module_name in module_names:
            __import__(app_name + '.' + package_name + '.' + module_name)

    def get_module_names(self) -> list[str]:
        module_paths = glob.glob(join(dirname(self.file_path), "*.py"))
        module_names = [basename(f)[:-3] for f in module_paths if isfile(f) and not f.endswith('__init__.py')]
        return module_names
