import pygame
#scale function
def load_and_scale(path: str, dimmensions: tuple):
    image = pygame.image.load(path).convert_alpha()
    image = pygame.transform.scale(image, dimmensions)
    return image


# Loading bullshit
screen = pygame.display.set_mode((400, 800))
pygame.display.set_caption("Run Teto run")
teto = pygame.Rect((170,400,45,55))
teto_image = load_and_scale("images\\stupid_fucking_teto.png", (70,70))
job_pipe = load_and_scale("images\\job_application.png",(70,300))
bg_img = load_and_scale("images\\city_background.jpg", (1600, 800))
silly_teto_img = load_and_scale("images\\silly teto.jpg", (400, 800))
teto_image_rect = teto_image.get_rect()
canos = []

#Physics and game states
running = True
acceleration = 0.5
speed = 0.2
y = 400
bg_pos = 0
jumping = False
clock = pygame.time.Clock()
delta_time = 0.1
game_state = 0
teto_rotation = 0

while running:
    # Check to determine game state
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Game state 0(intro/pause screen)
    if game_state == 0:
        screen.blit(silly_teto_img,(0,0))
        if key[pygame.K_SPACE] == True:
            game_state = 1
        pygame.display.flip()
        
    # Game state 1(game running)
    elif game_state == 1:

        # Jumping and teto position shenenigans
        mortal_teto = teto_image
        teto.y = y
        if key[pygame.K_SPACE] == True:
            if jumping:
                pass
            else:
                speed = -14
                jumping = True
        else:
            jumping = False
        if key[pygame.K_ESCAPE] == True:
            game_state = 0
        if teto.y >= 750:
            speed = 0
        else:
            speed += acceleration
            y += speed

        #Teto rotation
        if speed <0 :
            if teto_rotation <0:
                teto_rotation += acceleration*5
            else:
                teto_rotation += acceleration*3
        else:
            teto_rotation += -acceleration*3
        if teto_rotation > 30:
            teto_rotation = 30
        elif teto_rotation < -30:
            teto_rotation = -30
        mortal_teto = pygame.transform.rotate(mortal_teto, teto_rotation)
        
        # Background position
        bg_pos += -1
        if bg_pos <= -1200:
            bg_pos = 0
        # cano spawning
        if bg_pos % 100 == 0:
            canos.append(300)
        for cano in canos:
            if cano <= 0:
                canos.remove(cano)

        # Kill switch
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Drawing stuff on screen
        screen.blit(bg_img, (bg_pos,0))
        #pygame.draw.rect(screen, (255, 0, 0), teto)
        teto_image_rect.topleft = (teto.left-15, teto.top-9)
        screen.blit(mortal_teto, teto_image_rect)
        for i in range(0,len(canos)):
            cano = canos[i]
            screen.blit(job_pipe, (cano,500))
            canos[i] = cano-1
        pygame.display.flip()

        # No idea how this works but it makes it run smoother
        delta_time = clock.tick(60)
        delta_time = max(0.001, min(0.1, delta_time))




