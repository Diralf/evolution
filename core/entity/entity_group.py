import pygame
from pygame.sprite import Group


class EntityGroup(Group):

    def __init__(self, *sprites):
        super(EntityGroup, self).__init__(*sprites)

    def draw(self, surface):
        sprites = self.sprites()
        surface_blit = surface.blit
        surface_rect = surface.get_rect()

        sprite_depth = {}

        for sprite in sprites:
            pos = int(sprite.position.y)
            if surface_rect.y <= pos < surface_rect.h + sprite.rect.h:
                if pos not in sprite_depth:
                    sprite_depth[pos] = []
                sprite_depth[pos].append(sprite)

        for i in range(surface_rect.y, surface_rect.h + sprite.rect.h):
            if i in sprite_depth:
                for spr in sprite_depth[i]:
                    self.spritedict[spr] = surface_blit(spr.image, spr.rect)

        self.lostsprites = []

    def draw_debug(self, surface):
        for spr in self.sprites():
            pygame.draw.circle(surface, (255, 0, 0), (spr.rect.x, spr.rect.y), 3, 0)
            pygame.draw.circle(surface, (0, 255, 0), spr.position.get_point(), 4, 1)


