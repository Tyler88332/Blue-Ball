import os
os.chdir(os.path.dirname(os.path.abspath("C:/Users/m6rep/Downloads/python-projects/Blue ball movement/Pygame_test.py")))
import pygame
import time
import random
pygame.init()
pygame.joystick.init()
clock = pygame.time.Clock()
joysticks = []
from pygame.locals import *

ControllerIsBlue = True

EPVX = 0.0
EPVY = 0.0 
FPVX = 0.0
FPVY = 0.0
PVX = 0.0
PVY = 0.0
CD = 1000
input_time1 = 0
input_time2 = 0

    #sound effects
bounce_sfx = pygame.mixer.Sound("Sounds/basket-ball-bounce_tbc4yrJO.mp3")
jump_sfx = pygame.mixer.Sound("Sounds/sans-teleport-time-jump.mp3")
Todo_clap = pygame.mixer.Sound("Sounds/Aoi-Todo-Clap.mp3")
slash = pygame.mixer.Sound("Sounds/undertale-slash.mp3")
rezero = pygame.mixer.Sound("Sounds/re-zero-return.mp3")
        #random death sfx 1-8
death1 = pygame.mixer.Sound("Sounds/mungus_kill.mp3")
death2 = pygame.mixer.Sound("Sounds/geometry_death.mp3")
death3 = pygame.mixer.Sound("Sounds/undertale-death.mp3")
death4 = pygame.mixer.Sound("Sounds/gore-gush.mp3")
death5 = pygame.mixer.Sound("Sounds/roblox-death-sound-effect.mp3")
death6 = pygame.mixer.Sound("Sounds/fortnite_downed.mp3")


font = pygame.font.SysFont("Futura", 30)
pygame.display.set_caption("Blue Ball")

enemy = True
otherP = True
null = 0

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

# Source - https://stackoverflow.com):
def sqrt(x):
    if x == 0: return 0
    last_guess= x/2.0
    while True:
        guess= (last_guess + x/last_guess)/2
        if abs(guess - last_guess) < .000001: # example threshold
            return guess
        last_guess= guess
# stackflow code ends here

screen_width = 1920
screen_height = 1000
if screen_width < screen_height:
    Sscreen2 = screen_width
else:
    Sscreen2 = screen_height

Sscreen = Sscreen2/1080
Jump_height = 45*Sscreen #default = 45d
Speed = 3*Sscreen #default = 3 (aceleration)
Fall_speed = 1*Sscreen #defalt = 1
Jump_mult = 0.5 #default = 0.2
Gap_pix = 3*Sscreen #default = 3
Top_Speed = 54*Sscreen #default = 54
Friction = 0.95 #default = 0.95
Bouncyness = 0.5 #default = 0.5

if enemy == True:
    EJump_height = 45*Sscreen #default = 45
    ESpeed = 1*Sscreen #default = 1 (aceleration)
    EFall_speed = 1*Sscreen #defalt = 1
    EGap_pix = 3*Sscreen #default = 3
    ETop_Speed = 100*Sscreen #default = 54
    EFriction = 0.95 #default = 0.95
    EBouncyness = 0.55 #default = 0.55
shape = pygame.Rect((((screen_width/2)-(screen_width/8)), ((screen_height/2)-(screen_height/8)), (Sscreen2/27), (Sscreen2/27)))
Eshape = pygame.Rect((((screen_width/2)-(screen_width/8) + 70), ((screen_height/2)-(screen_height/8)), (Sscreen2/27), (Sscreen2/27)))
x_pos = float(shape.x)
y_pos = float(shape.y)
Ex_pos = float(Eshape.x)
Ey_pos = float(Eshape.y)
Fx_pos = 0.0
Fy_pos = 0.0
text_font = pygame.font.SysFont("Arial", 30)
gp45 = 0
run = True
while run:
    if gp45 > 0:
        randeathsfx = random.randint(1,6)
        if randeathsfx == 1:
            death1.play()
        elif randeathsfx == 2:
            death2.play()
        elif randeathsfx == 3:
            death3.play()
        elif randeathsfx == 4:
            death4.play()
        elif randeathsfx == 5:
            death5.play()
        elif randeathsfx == 6:
            death6.play()
        time.sleep(0.35)
        rezero.play()
        time.sleep(0.65)

    EPVX = 0.0
    EPVY = 0.0 
    FPVX = 0.0
    FPVY = 0.0
    PVX = 0.0
    PVY = 0.0
    shape.x = ((screen_width/2)-(screen_width/8))
    shape.y = ((screen_height/2)-(screen_height/8))
    Eshape.x = ((screen_width/2)-(screen_width/8) + 70)
    Eshape.y = ((screen_height/2)-(screen_height/8))
    x_pos = float(shape.x)
    y_pos = float(shape.y)
    Ex_pos = float(Eshape.x)
    Ey_pos = float(Eshape.y)
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)

    overlay = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)    
    overlay.fill((0, 0, 0, 10))
    running = True

    if pygame.joystick.get_count() > 0:
        controller = pygame.joystick.Joystick(0)
        controller.init()

    analog_x = 0.0

    while running:
        gp45 = 1
        raninsult = random.randint(1, 5)
        if raninsult == 1:
            raninsult = ("Ez")
        if raninsult == 2:
            raninsult = ("lol")
        if raninsult == 3:
            raninsult = ("L ratio")
        if raninsult == 4:
            raninsult = ("Where Are You Going")
        if raninsult == 5:
            raninsult = ("You're Lost")
        
        dt = clock.tick(60) / 1000.0
        screen.blit(overlay, (0, 0))
        pygame.draw.ellipse(screen, (0, 0, 255), shape)
        pygame.draw.ellipse(screen, (255, 0, 0), Eshape)
        key = pygame.key.get_pressed()
        draw_text("Controllers: " + str(pygame.joystick.get_count()), font, pygame.Color("azure"), 10, 10)
    
    # 1. PUMP AND READ EVENTS FIRST
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                run = False 

            if event.type == VIDEORESIZE:
                screen_height = event.h
                screen_width = event.w
                screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
                overlay = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
                overlay.fill((0, 0, 0, 10))
                if screen_width < screen_height:
                    Sscreen2 = screen_width
                else:
                    Sscreen2 = screen_height
                Sscreen = Sscreen2/1080
                Jump_height = 45*Sscreen #default = 45d
                Speed = 3*Sscreen #default = 3 (aceleration)
                Fall_speed = 1*Sscreen #defalt = 1
                Jump_mult = 0.5 #default = 0.2
                Gap_pix = 3*Sscreen #default = 3
                Top_Speed = 54*Sscreen #default = 54
                Friction = 0.95 #default = 0.95
                Bouncyness = 0.5 #default = 0.5
                if enemy == True:
                    EJump_height = 45*Sscreen #default = 45
                    ESpeed = 1*Sscreen #default = 1 (aceleration)
                    EFall_speed = 1*Sscreen #defalt = 1
                    EGap_pix = 3*Sscreen #default = 3
                    ETop_Speed = 100*Sscreen #default = 54
                    EFriction = 0.95 #default = 0.95
                    EBouncyness = 0.55 #default = 0.55
                    shape = pygame.Rect((((screen_width/2)-(screen_width/8)), ((screen_height/2)-(screen_height/8)), (Sscreen2/27), (Sscreen2/27)))
                    Eshape = pygame.Rect((((screen_width/2)-(screen_width/8) + 70), ((screen_height/2)-(screen_height/8)), (Sscreen2/27), (Sscreen2/27)))

        # --- KEYBOARD INPUTS ---
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if y_pos >= (screen_height - ((45*Sscreen)+Gap_pix)):
                        PVY = PVY - Jump_height
                        PVX = PVX + (PVX * Jump_mult)
                        jump_sfx.play()
                        if key[pygame.K_a] == True:
                            PVX *= PVX
                            PVX = sqrt(PVX)
                            PVX *= -1
                        elif key[pygame.K_d] == True:
                            PVX *= PVX
                            PVX = sqrt(PVX)
                if event.key == pygame.K_s:
                    draw_text(raninsult, text_font, (255, 255, 255), x_pos, y_pos-Sscreen2/27)
                elif event.key == pygame.K_DOWN:
                    draw_text(str(raninsult), text_font, (255, 255, 255), Ex_pos, Ey_pos-Sscreen2/27)
            
            # Blue Ball Positional Swap Ability Logic
                if event.key == pygame.K_f:
                    if (pygame.time.get_ticks() - input_time1) > CD:
                        Fx_pos = x_pos
                        Fy_pos = y_pos
                        x_pos = Ex_pos
                        y_pos = Ey_pos
                        Ex_pos = Fx_pos
                        Ey_pos = Fy_pos
                        Todo_clap.play()
                        screen.fill((0, 0, 40))
                        input_time1 = pygame.time.get_ticks()

            # Red Ball Momentum/Vector Swap Ability Logic
                if event.key == pygame.K_UP and otherP == True:
                    if (pygame.time.get_ticks() - input_time2) > CD:
                        FPVX = PVX
                        FPVY = PVY
                        PVX = EPVX
                        PVY = EPVY
                        EPVX = FPVX
                        EPVY = FPVY
                        slash.play()
                        screen.fill((40, 0, 0))
                        input_time2 = pygame.time.get_ticks()
    
                if event.key == pygame.K_e:
                    if otherP == False:
                        otherP = True
                    else:
                        otherP = False

            # --- CONTROLLER INPUTS ---
            elif event.type == pygame.JOYBUTTONDOWN:
                if pygame.joystick.get_count() > 0:
                    analog_x = controller.get_axis(0)

            # Button 0 (A Button) Jump Logic for Blue Ball Only
                if event.button == 0 and ControllerIsBlue == True:
                    if y_pos >= (screen_height - ((45*Sscreen)+Gap_pix)):
                        PVY = PVY - Jump_height
                        PVX = PVX + (PVX * Jump_mult)
                        jump_sfx.play()

                    # Check direction based on analog stick tilt during the jump frame
                        if analog_x < -0.1:  # Tilting Left
                            PVX *= PVX
                            PVX = sqrt(PVX)
                            PVX *= -1
                        elif analog_x > 0.1:  # Tilting Right
                            PVX *= PVX
                            PVX = sqrt(PVX)
            
            # Button 1 (B Button) Insult System Logic
                elif event.button == 1:
                    if ControllerIsBlue == True:
                        draw_text(raninsult, text_font, (255, 255, 255), x_pos, y_pos-40)
                    else:
                        draw_text(str(raninsult), text_font, (255, 255, 255), Ex_pos, Ey_pos-40)

            # Button 2 (X Button) Ability for Blue Ball (Positional Swap)
                elif event.button == 2 and ControllerIsBlue == True:
                    if (pygame.time.get_ticks() - input_time1) > CD*1.25:
                        Fx_pos = x_pos
                        Fy_pos = y_pos
                        x_pos = Ex_pos
                        y_pos = Ey_pos
                        Ex_pos = Fx_pos
                        Ey_pos = Fy_pos
                        input_time1 = pygame.time.get_ticks()

                # Button 2 (X Button) Ability for Red Ball (Momentum Vector Swap)
                elif event.button == 2 and ControllerIsBlue == False and otherP == True:
                    if (pygame.time.get_ticks() - input_time2) > CD*1.25:
                        FPVX = PVX
                        FPVY = PVY
                        PVX = EPVX
                        PVY = EPVY
                        EPVX = FPVX
                        EPVY = FPVY
                        input_time2 = pygame.time.get_ticks()

            # Button 3 (Y Button) Logic - Sets controller to False (Swaps to Red Ball)
                elif event.button == 3:
                    ControllerIsBlue = False

    # 2. UPDATE CONTINUOUS ANALOG AXIS STATE FOR REGULAR MOVEMENT
        if pygame.joystick.get_count() > 0:
            analog_x = controller.get_axis(0)

    # --- MOVEMENT & PHYSICS ---
    # Blue Ball Left
        if key[pygame.K_a] == True or (analog_x < -0.1 and ControllerIsBlue == True):
            if y_pos >= (screen_height - ((45*Sscreen)+Gap_pix)):
                if PVX != (Top_Speed * -1) or PVX > (Top_Speed * -1):
                    PVX = PVX - Speed

    # Blue Ball Right
        if key[pygame.K_d] == True or (analog_x > 0.1 and ControllerIsBlue == True):
            if y_pos >= (screen_height - ((45*Sscreen)+Gap_pix)):
                if PVX != Top_Speed or PVX < Top_Speed:
                    PVX = PVX + Speed

        if y_pos >= (screen_height - ((40*Sscreen)+Gap_pix)):
            if PVY > (Sscreen2/27)/4:
                y_pos = screen_height - ((40*Sscreen)+Gap_pix)
                PVY = PVY * - Bouncyness
                bounce_sfx.play()

            else:
                y_pos = screen_height - ((40*Sscreen)+Gap_pix)
        else:
            if y_pos < (screen_height - ((40*Sscreen)+Gap_pix)):
                PVY = PVY + Fall_speed
        if y_pos >= (screen_height - ((40*Sscreen)+Gap_pix)):
            PVX = PVX * Friction

        x_pos += (PVX * dt) * 10
        y_pos += (PVY * dt) * 10
        shape.x = int(x_pos)
        shape.y = int(y_pos)

        if Ey_pos >= (screen_height - ((40*Sscreen)+EGap_pix)):
            if EPVY > (Sscreen2/27)/4:
                Ey_pos = screen_height - ((40*Sscreen)+EGap_pix)
                EPVY = EPVY * - EBouncyness
                bounce_sfx.play()

            else:
                Ey_pos = screen_height - ((40*Sscreen)+EGap_pix)
        else:
            if Ey_pos < (screen_height - ((40*Sscreen)+EGap_pix)):
                EPVY = EPVY + EFall_speed

        if otherP == False:
            if Ex_pos > x_pos:
                if Ey_pos >= (screen_height - ((45*Sscreen)+EGap_pix)):
                    if EPVX != (ETop_Speed * -1) or EPVX > (ETop_Speed * -1):
                        EPVX = EPVX - ESpeed
            if Ex_pos < x_pos:
                    if Ey_pos >= (screen_height - ((45*Sscreen)+EGap_pix)):
                        if EPVX != (ETop_Speed) or EPVX > (ETop_Speed):
                            EPVX = EPVX + ESpeed

        
        elif otherP == True:
            # Red Ball Left
            if key[pygame.K_LEFT] == True or (analog_x < -0.1 and ControllerIsBlue == False):
                if Ey_pos >= (screen_height - ((45*Sscreen)+EGap_pix)):
                    if EPVX != (ETop_Speed * -1) or EPVX > (ETop_Speed * -1):
                        EPVX = EPVX - ESpeed

        # Red Ball Right
            if key[pygame.K_RIGHT] == True or (analog_x > 0.1 and ControllerIsBlue == False):
                if Ey_pos >= (screen_height - ((45*Sscreen)+EGap_pix)):
                    if EPVX != (ETop_Speed) or EPVX > (ETop_Speed):
                        EPVX = EPVX + ESpeed
    
        if x_pos < Ex_pos + (30*Sscreen) and x_pos > Ex_pos - (30*Sscreen) and y_pos < Ey_pos + (30*Sscreen) and y_pos > Ey_pos - (30*Sscreen):
            running = False
        
        Ex_pos += (EPVX * dt) * 10
        Ey_pos += (EPVY * dt) * 10
        Eshape.x = int(Ex_pos) 
        Eshape.y = int(Ey_pos)
        if x_pos > screen_width:
            x_pos = 0
        if x_pos < 0:
            x_pos = screen_width
        if Ex_pos > screen_width:
            Ex_pos = 0
        if Ex_pos < 0:
            Ex_pos = screen_width
        
        pygame.display.update()
pygame.quit()