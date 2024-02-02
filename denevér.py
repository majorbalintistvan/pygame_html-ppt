import pygame
import time

pygame.init()
# képernyő hossza
width = 1200
# képernyő magassága
height = 860
screen_res = (width, height)

pygame.display.set_caption("Repülő denevér")
screen = pygame.display.set_mode(screen_res)
time_start = time.time()
clock = pygame.time.Clock()
# színek
piros = (255, 0, 0)
Háttérkép = pygame.image.load("kastély.png")
Háttér=pygame.transform.scale(Háttérkép,(1600,1080))
fehér = (255, 255, 255)

# kiírás
game_font = pygame.font.SysFont("Verdana", 60)
text_surf = game_font.render("GAME", True, fehér)
text_rect = text_surf.get_rect(center=(width / 2, height / 2))
# denevér kép animáció összerakása
bat1 = pygame.image.load("denevér1.png").convert_alpha()
bat2 = pygame.image.load("denevér2.png").convert_alpha()
bat3 = pygame.image.load("denevér3.png").convert_alpha()
bat4 = pygame.image.load("denevér4.png").convert_alpha()
bat5 = pygame.image.load("denevér3.png").convert_alpha()
bat6 = pygame.image.load("denevér2.png").convert_alpha()
bat = [bat1, bat2, bat3, bat4, bat5, bat6]
bat_index = 0
bat_rect = bat[bat_index].get_rect(midleft=(200, 140))
számláló = 0
# milyen gyors
# gyorsaság = [X tengelyen, Y tengelyen]
gyorsaság = [5.3, 6.2]
score = 0
# game loop
while True:
    # event loop
    for event in pygame.event.get():
        # check if a user wants to exit the game or not
        if event.type == pygame.QUIT:
            exit()

    # idő számlálás
    game_time = str(int(time.time() - time_start))
    time_surf = game_font.render("Idő: " + game_time, True, fehér)
    time_rect = time_surf.get_rect(topleft=(10, 10))

    score_surf = game_font.render("Falhoz érések száma: " + str(score), True, fehér)
    score_rect = score_surf.get_rect(topright=(width - 10, 10))

    # háttér kitoltése
    screen.blit(Háttér,(0,0))
    # bat animáció
    számláló += 1
    if számláló % 5 == 0:
        bat_index += 1
    if bat_index > len(bat) - 1:
        bat_index = 0

    # denevér mozog
    bat_rect = bat_rect.move(gyorsaság)
    # ezen a mentén fog a falunk mozogni
    # ha a denevér kimely a képből jöjjön vissza
    if bat_rect.left <= 0 or bat_rect.right >= width:
        gyorsaság[0] = -gyorsaság[0]
        score += 1
    if bat_rect.top <= 0 or bat_rect.bottom >= height:
        gyorsaság[1] = -gyorsaság[1]
        score += 1

    screen.blit(bat[bat_index], bat_rect)
    screen.blit(time_surf, time_rect)
    screen.blit(score_surf, score_rect)
    # frissiteni a képernyőt
    pygame.display.update()
    clock.tick(60)
pygame.quit()
