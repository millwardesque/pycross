class Image:
    _name: str
    def __init__(self, image_name: str):
        self._name = image_name

    def name(self) -> str:
        return self._name