import pygame, sys
from bullet import Bullet
from mega_alien import Mega_alien
import time 


def events(screen, mega_gun, bullets):
    """обработка событий"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # кнопка вправо
            if event.key == pygame.K_d:
                mega_gun.move_right = True
            # кнопка влево
            elif event.key == pygame.K_a:
                mega_gun.move_left = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, mega_gun)
                bullets.add(new_bullet)

        elif event.type == pygame.KEYUP:
            # кнопка вправо
            if event.key == pygame.K_d:
                mega_gun.move_right = False
            # кнопка влево
            elif event.key == pygame.K_a:
                mega_gun.move_left = False



def update_screen(bg_color, screen, stats, score, mega_gun, aliens, bullets):
    """обновление экрана"""
    screen.fill(bg_color)
    score.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    mega_gun.output_gun()
    aliens.draw(screen)
    pygame.display.flip()


def update_bullets(screen, stats, score, aliens, bullets):
    """обновлеие позиций пуль"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += 10 * len(aliens)
        score.image_score()
        chek_high_score(stats, score)
        score.image_guns()

    if len(aliens) == 0:
        bullets.empty()
        create_army(screen, aliens)


def gun_kill(stats, screen, score, mega_gun, aliens, bullets):
    """столкновение пушки с пришельцами"""
    if stats.guns_left > 0:
        stats.guns_left -= 1
        score.image_guns()
        aliens.empty()
        bullets.empty()
        create_army(screen, aliens)
        mega_gun.create_gun()
        time.sleep(2)
    else:
        stats.run_game = False
        sys.exit()

    

def update_aliens(stats, screen, score, mega_gun, aliens, bullets):
    """обновление позиции пришельцев"""
    aliens.update()
    if pygame.sprite.spritecollideany(mega_gun, aliens):
        gun_kill(stats, screen, score, mega_gun, aliens, bullets)
    aliens_chek(stats, screen, score, mega_gun, aliens, bullets)


def aliens_chek(stats, screen, score, mega_gun, aliens, bullets):
    """проверка на косание нижней части экрана пришельцами"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom > screen_rect.bottom:
            gun_kill(stats, screen, score, mega_gun, aliens, bullets)
            break



def create_army(screen, aliens):
    """создание армии пришельцев"""
    alien = Mega_alien(screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    number_alien_x = int((700 - 2 * alien_width) / alien_width)
    alien_height = alien.rect.height
    number_alien_y = int((800 - 100 - 2 * alien_height) / alien_height)

    for row_number in range(number_alien_y - 1):
        for alien_number in range(number_alien_x):
            alien = Mega_alien(screen)
            alien.x = alien_width + (alien_width * alien_number)
            alien.y = alien_height + (alien_height * row_number)
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height + (alien.rect.height * row_number)
            aliens.add(alien)

def chek_high_score(stats, score):
    """проверка новых рекордов"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        score.image_high_score()
        with open('my_game/high_score.txt', 'w') as file:
            file.write(str(stats.high_score))

