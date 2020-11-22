from image import Image
import os
import pygame
from rendering_engine import RenderingEngine

class PygameRenderingEngine(RenderingEngine):
    _screen: pygame.Surface
    _font: pygame.font.Font
    _image_cache: object


    def __init__(self, width: int, height: int, font_size: int):
        super().__init__(width, height, font_size)

        pygame.init()
        self._screen = pygame.display.set_mode([width, height])
        self._font = pygame.font.SysFont("Arial", 14)
        self._image_cache = {}


    def _load_image(self, image: Image):
        if not os.path.isfile(image.full_path()):
            raise ValueError(f"Image at {image.full_path()} doesn't exist")

        if image.name not in self._image_cache:
            self._image_cache[image.name()] = pygame.image.load(image.full_path())

        return self._image_cache[image.name()]

    def clear(self):
        self._screen.fill(pygame.Color("black"))

    def end_render(self):
        pygame.display.flip()

    def draw_static_image(self, img: Image, x: int, y: int):
        native_img = self._load_image(img)
        self._screen.blit(native_img, [x, y])

    def draw_text(self, text: str, x: int, y: int, color: list=None):
        if color is None:
            color = [255, 255, 255]

        text_surface = self._font.render(text, True, color)
        self._screen.blit(text_surface, [x, y])

    def get_text_width(self, text, render_horizontal: bool=True):
        if render_horizontal:
            return self._font.size(text)[0]
        else:
            max_width = 0
            for c in text:
                width = self._font.size(c)[0]
                if width > max_width:
                    max_width = width

            return max_width

    def get_text_height(self, text, render_horizontal: bool=True):
        if render_horizontal:
            return self._font.size(text)[1]
        else:
            total_height = 0
            for c in text:
                total_height += self._font.size(c)[1]

            return total_height
