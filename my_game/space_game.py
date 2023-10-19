import pygame, controls
from mega_gun import Mega_gun
from pygame.sprite import Group
from stats import Stats
from scores import Scores


def run():

    pygame.init()
    screen = pygame.display.set_mode((700, 790))
    pygame.display.set_caption("Space Guards")
    bg_color = (0, 0, 0)
    mega_gun = Mega_gun(screen)
    bullets = Group()
    aliens = Group()
    controls.create_army(screen, aliens)
    stats = Stats()
    score = Scores(screen, stats)


    while True:
        controls.events(screen, mega_gun, bullets)
        if stats.run_game:
            mega_gun.update_gun()
            controls.update_screen(bg_color, screen, stats, score, mega_gun, aliens, bullets) 
            controls.update_bullets(screen, stats, score, aliens, bullets)
            controls.update_aliens(stats, screen, score, mega_gun, aliens, bullets)



run()