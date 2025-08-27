import pygame
pygame.init
# Scale function
def load_and_scale(path: str, dimmensions: tuple):
    image = pygame.image.load(path).convert_alpha()
    image = pygame.transform.scale(image, dimmensions)
    return image

# Jumping check
def jumping_check(key):
    global jumping
    global speed
    global y
    teto.y = y
    if key[pygame.K_SPACE]:
        if jumping:
            pass
        else:
            speed = -14
            jumping = True
    else:
        jumping = False
    if key[pygame.K_ESCAPE]:
        return 0
    if teto.y >= 750:
        speed = 0
    else:
        speed += acceleration
        y += speed

# Calculating teto angle
def teto_angle():
    global speed
    global teto_rotation
    if speed <0:
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
    teto_image_rect.topleft = (teto.left-15, teto.top-9)
    mortal_teto = teto_image
    mortal_teto = pygame.transform.rotate(mortal_teto, teto_rotation)
    return mortal_teto

# Calculating background postion
def background_position():
    global bg_pos
    bg_pos += game_speed
    if  bg_pos <= -1200:
        bg_pos = 0
    return bg_pos

# Pipe Spawning
def pipe_spawning():
    global canos
    global cano
    global cano_tick
    if round(bg_pos,-1) % 200 == 0 and cano_tick == 0:
        canos.append(500)
        cano_tick = 1
    if round(bg_pos,-1) % 200 != 0:
        cano_tick = 0
    for cano in canos:
        if cano <= -100:
            canos.remove(cano)

#time shenenigans
def time():
    global delta_time
    global clock
    delta_time = clock.tick(60)
    delta_time = max(0.001, min(0.1, delta_time))

#Drawing everything on screen
def drawing_screen():
    global canos
    global cano
    screen.blit(bg_img, (background_position(),0))
    #pygame.draw.rect(screen, (255, 0, 0), teto)
    screen.blit(teto_angle(), teto_image_rect)
    for i in range(0,len(canos)):
        cano = canos[i]
        screen.blit(job_pipe, (cano,500))
        canos[i] = cano+game_speed
    pygame.display.flip()

#Kill switch
def kill_switch():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False




# Window
screen = pygame.display.set_mode((400, 800))
pygame.display.set_caption("Run Teto run")

# Loading bullshit
teto_image = load_and_scale("images\\stupid_fucking_teto.png", (70,70))
job_pipe = load_and_scale("images\\beer-removebg-preview.png",(70,300))
pipe_rect = job_pipe.get_rect()
bg_img = load_and_scale("images\\city_background.jpg", (1600, 800))
silly_teto_img = load_and_scale("images\\silly teto.jpg", (400, 800))

#Defining important stuff
teto = pygame.Rect((170,400,45,55))
teto_image_rect = teto_image.get_rect()
job_pipe.set_colorkey((255,255,255))
bg_img_rect = bg_img.get_rect()
cano_tick = 0
canos = []

#Physics and game states
running = True
acceleration = 0.7
speed = 0.2
y = 400
bg_pos = 0
game_speed = -3
jumping = False
clock = pygame.time.Clock()
delta_time = 0.1
game_state = 0
teto_rotation = 0

#Function of game state 0
def draw_start_screen(key):
    screen.blit(silly_teto_img,(0,0))
    if key[pygame.K_SPACE] == True:
        return 1
    pygame.display.flip()
    return 0

#Function of game state 1
def draw_game():
    jumping_check(key)
    pipe_spawning()
    drawing_screen()
    time()
    return 1

#Loop
while running:
    # Check to determine game state
    key = pygame.key.get_pressed()

    # Game state 0(intro/pause screen)
    if game_state == 0:
        kill_switch()
        game_state = draw_start_screen(key)
        
    # Game state 1(game running)
    elif game_state == 1:
        kill_switch()
        game_state = draw_game()





