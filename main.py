import pygame
import random
pygame.init()
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
    mortal_teto = pygame.transform.rotate(teto_image, teto_rotation)

    custom_center = (teto.centerx -5, teto.centery -7)
    rotated_rect = mortal_teto.get_rect(center=custom_center)
    teto_image_rect.center = rotated_rect.center
    mortal_teto.set_colorkey((255,255,255))
    return mortal_teto

# Calculating background postion
def background_position():
    global bg_pos
    bg_pos += game_speed
    if  bg_pos <= -1200:
        bg_pos = 0
    return bg_pos
# Collision objects
class CollisionObjectt():
    def __init__(self, x, y, h, w):
        self.x = x
        self.y = y
        self.h = h
        self.w = w
    def move(self):
        self.x += game_speed

# Pipe Spawning
def pipe_spawning():
    global canos
    global cano
    global cano_tick
    if round(bg_pos,-1) % 250 == 0 and cano_tick == 0:
        y = random.randint(350,750)
        canos.append(pygame.Rect(500,y, 69, 550))
        canos2.append(pygame.Rect(500,-770+y,69,550))
        cano_tick = 1
    if round(bg_pos,-1) % 250 != 0:
        cano_tick = 0
    for cano in canos:
        if cano.x <= -100:
            canos.remove(cano)
    for cano in canos2:
        if cano.x <= -100:
            canos2.remove(cano)

#time shenenigans
def time():
    global delta_time
    global clock
    delta_time = clock.tick(60)
    delta_time = max(0.001, min(0.1, delta_time))

#Detecting teto collision
def tetollision():
    for cano in canos:
        if teto.colliderect(cano):
            return True
    for cano in canos2:
        if teto.colliderect(cano):
            return True
    if teto.y >= 750:
        return True
    return False

#Drawing everything on screen
def drawing_screen():
    global canos
    global cano
    screen.blit(bg_img, (background_position(),0))
    screen.blit(teto_angle(), teto_image_rect)
    for cano in canos:
        cano.x += game_speed
        screen.blit(job_pipe, (cano.x -5, cano.y-3))
    for cano in canos2:
        cano.x += game_speed
        screen.blit(job_pipe_r, (cano.x -5, cano.y-200)) 
    pygame.display.flip()

#Kill switch
def kill_switch():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#Reset function

def made_in_heaven():
    global canos
    global canos2
    global y
    global speed
    global bg_pos
    global teto_rotation
    global jumping
    
    canos = []
    canos2 = []
    y = 400
    speed = 0.2
    bg_pos = 0
    jumping = False
    teto_rotation = 0

def dumb_fuck():
    global dumb_position
    global dumber_position
    global dumb_fuck_speedX
    global dumb_fuck_speedY
    dumb_position += dumb_fuck_speedX
    dumber_position += dumb_fuck_speedY
    if dumb_position >= 300:
        dumb_fuck_speedX = -(random.randint(2,4))
    elif dumb_position <= 0:
        dumb_fuck_speedX = (random.randint(2,4))
    if dumber_position >= 600:
        dumb_fuck_speedY = -(random.randint(2,4))
    if dumber_position <= 0:
        dumb_fuck_speedY = (random.randint(2,4))
    screen.blit(teto_dumb, (dumb_position,dumber_position))



# Window
screen = pygame.display.set_mode((400, 800))
pygame.display.set_caption("Run Teto run")

# Loading bullshit
teto_image = load_and_scale("images\\stupid_fucking_teto.png", (60,70))
job_pipe = load_and_scale("images\\beer-removebg-preview.png",(80,750))
job_pipe_r = pygame.transform.flip(job_pipe, True, True)
bg_img = load_and_scale("images\\city_background.jpg", (1600, 800))
silly_teto_img = load_and_scale("images\\silly teto.jpg", (400, 800))
teto_laugh = load_and_scale("images\\teto-kasane.png", (400, 800))
teto_dumb = load_and_scale("images\\dumb fuck.jpeg", (100, 200))


#Defining important stuff
teto = pygame.Rect((170,400,30,55))
teto_image_rect = teto_image.get_rect()
job_pipe.set_colorkey((255,255,255))
job_pipe_r.set_colorkey((255,255,255))
bg_img_rect = bg_img.get_rect()
cano_tick = 0
canos = []
canos2 = []

#Physics and game states
dumb_position = 1
dumber_position = 200
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
dumb_fuck_speedX = 2
dumb_fuck_speedY = 2
teto_rotation = 0

#Function of game state 0
def draw_start_screen(key):
    screen.blit(silly_teto_img,(0,0))
    if key[pygame.K_SPACE] == True:
        return 1
    return 0

#Function of game state 1
def draw_game():
    if key[pygame.K_ESCAPE]:
        return 0
    jumping_check(key)
    pipe_spawning()
    drawing_screen()
    if tetollision():
        return 2
    time()
    return 1

#Game state 2
def draw_loser_screen():
    screen.blit(teto_laugh,(0,0))
    dumb_fuck()
    print(dumb_position)
    if key[pygame.K_SPACE]:
        made_in_heaven()
        return 1
    time()
    return 2


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

    elif game_state == 2:
        kill_switch()
        game_state = draw_loser_screen()


    pygame.display.flip()



