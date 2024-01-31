# FONTOS amíg még hátra vannak ebből a programból:
# - Lecserélni valamire a dvd logót(ha akarjuk)
import pygame
import time

pygame.init()
# képernyő hossza
width = 1600
# képernyő magassága
height = 1080
screen_res = (width, height)

pygame.display.set_caption("Pattogó dvd")
screen = pygame.display.set_mode(screen_res)
time_start = time.time()
clock = pygame.time.Clock()
# színek
piros = (255, 0, 0)
fekete = (0, 0, 0)
fehér = (255, 255, 255)

#kiírás
game_font = pygame.font.SysFont('Verdana', 60)
text_surf = game_font.render('GAME', True, fehér)
text_rect = text_surf.get_rect(center=(width / 2, height / 2))
#dvd kép animáció összerakása
dvdkép1 = pygame.image.load("dvd.png")
dvdkép2= pygame.image.load("dvd2.png")
dvdkép3= pygame.image.load("dvd3.png")
dvdkép4= pygame.image.load("dvd4.png")
dvd1 = pygame.transform.scale(dvdkép1, (240, 160)).convert_alpha()
dvd2 = pygame.transform.scale(dvdkép2, (240, 160)).convert_alpha()
dvd3 = pygame.transform.scale(dvdkép3, (240, 160)).convert_alpha()
dvd4 = pygame.transform.scale(dvdkép4, (240, 160)).convert_alpha()
dvd=[dvd1,dvd2,dvd3,dvd4]
dvd_index=0
dvd_rect = dvd[dvd_index].get_rect(midleft=(240, 160))
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

    #idő számlálás
    game_time = str(int(time.time() - time_start))
    time_surf = game_font.render('Idő: ' + game_time, True, fehér)
    time_rect = time_surf.get_rect(topleft=(10,10))

    score_surf = game_font.render('Falhoz érések száma: ' + str(score), True, fehér)
    score_rect = score_surf.get_rect(topright=(width - 10, 10))

    # háttér kitoltése
    screen.fill(fekete)
    #dvd animáció
    # dvd mozog
    dvd_rect = dvd_rect.move(gyorsaság)
    # mostmár a dvd közepe (101,101)
    # ezen a mentén fog a falunk mozogni
    # ha a dvd kimely a képből jöjjön vissza
    if dvd_rect.left <= 0 or dvd_rect.right >= width:
        gyorsaság[0] = -gyorsaság[0]
        dvd_index+=1
        score+=1
    if dvd_rect.top <= 0 or dvd_rect.bottom >= height:
        gyorsaság[1] = -gyorsaság[1]
        dvd_index+=1
        score+=1

    if dvd_index>len(dvd)-1:
        dvd_index=0
    
    screen.blit(time_surf, time_rect)
    screen.blit(score_surf,score_rect)
    screen.blit(dvd[dvd_index], dvd_rect)
    # frissiteni a képernyőt
    pygame.display.update()
    clock.tick(60)
pygame.quit()
