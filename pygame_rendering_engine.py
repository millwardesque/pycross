from image import Image
import os
import pygame
from rendering_engine import RenderingEngine

class PygameRenderingEngine(RenderingEngine):
    _screen: pygame.Surface
    _font: pygame.font.Font
    _image_cache: object


    def __init__(self, width: int, height: int):
        super().__init__(width, height)

        pygame.init()
        self._screen = pygame.display.set_mode([width, height])
        self._font = pygame.font.SysFont("Arial", 14)
        self._image_cache = {}


    def _load_image(self, image: Image):
        if image.name not in self._image_cache:
            self._image_cache[image.name()] = pygame.image.load(image.name())

        return self._image_cache[image.name()]

    def clear(self):
        self._screen.fill(pygame.Color("black"))

    def flip(self):
        pygame.display.flip()

    def draw_static_image(self, img: Image, x: int, y: int):
        native_img = self._load_image(img)
        self._screen.blit(native_img, [x, y])

    def draw_text(self, text: str, x: int, y: int):
        text_surface = self._font.render(text, True, pygame.Color("white"))
        self._screen.blit(text_surface, [x, y])

