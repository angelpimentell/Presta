from os.path import dirname, basename, isfile, join
import glob


class Package:
    def __init__(self, file_path):
        self.file_path = file_path

    def import_all_modules_from_models(self):
        package_name = self.file_path.split('\\')[-3]
        modules_path = glob.glob(join(dirname(self.file_path), "*.py"))
        modules_name = [basename(f)[:-3] for f in modules_path if isfile(f) and not f.endswith('__init__.py')]
        for module in modules_name:
            __import__(package_name + '.models.' + module)
