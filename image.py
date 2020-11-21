import os

class Image:
    _name: str
    _directory: str

    def __init__(self, image_name: str, directory: str=''):
        self._name = image_name
        self._directory = directory

    def name(self) -> str:
        return self._name

    def directory(self) -> str:
        return self._directory

    def full_path(self) -> str:
        return os.path.join(self._directory, self._name)
