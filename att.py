import pygame
from sys import exit #might not need this is using the boolean method
from random import randint
pygame.init() #initializes

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 2

            screen.blit(mob_surface,obstacle_rect)
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        return obstacle_list
    else: return []

def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect): return False

screen = pygame.display.set_mode((700,630))
pygame.display.set_caption('Slime Slayer') #Chanes title of window
clock = pygame.time.Clock() #To deal with time and framerate?

#Text
font = pygame.font.Font('Font.ttf', 60)
s_font = pygame.font.Font('Font.ttf', 20)

test_surface = pygame.image.load('background.png').convert()
test_surface = pygame.transform.scale(test_surface,(test_surface.get_width()*.7, test_surface.get_height()*.7))
#surf_rect = test_surface.get_rect(center =(0,0))
game_active = False

#Obstacle
mob_surface = pygame.image.load('Sprites/Slime/Side/Slime.png').convert_alpha()
mob_surface = pygame.transform.scale(mob_surface,(mob_surface.get_width()*.3, mob_surface.get_height()*.3))

obstacle_rect_list = []
#Text
coin_surface = font.render('$0', False, (214, 209, 69))
coin_rect = coin_surface.get_rect(topleft = (50, 15))
gameover_surf1 = font.render('GAME OVER',False, 'White')
over_rect = gameover_surf1.get_rect(midtop = (360, 70))
gameover_surf2 = s_font.render('Press [Spacebar] to start', False,'White')
over_rect2 = gameover_surf2.get_rect(center = (360, 400))
game_name = font.render('Slime Slayer', False, 'White')
name_rect = game_name.get_rect(midtop = (360, 100))




# mob_rect = mob_surface.get_rect(topleft = (10,250)) Not needed since the object_movemnt function spawns them in?


player_surface = pygame.image.load("Sprites/SwordSp1.png").convert_alpha()
player_surface = pygame.transform.scale(player_surface,(player_surface.get_width()*.4, player_surface.get_height()*.4))
player_rect = player_surface.get_rect(midtop = (100,175)) #pygame.Rect(left, top, width, height). getRect(gets the size of the variable/object)
#get_rect(area,(x,y)) The area changes the center of which the rect is moved. For example from center to middle bottom can be used to place image surfaces on the ground " The ultimate introduction to Pygame" 57:55

#test_surface = pygame.Surface((100,200)) 'Surface' must be capitalized
#test_surface.fill("Blue") sets the surface colour to blue

#Timer
obstacle_timer = pygame.USEREVENT + 1 #+1 is to avoid the preset events in pygame
pygame.time.set_timer(obstacle_timer, 2000) #triggers event and determines how often the even should be triggered. Triggers event every 1000 milli seconds (1second)

while True:
    for event in pygame.event.get(): #check through "event"s based what event was update from the "get()" function
        if event.type == pygame.QUIT: #meaning if the x button is 
            pygame.quit() #closes the game. Uninitializes, causes an error by itself
            exit() #ends any code that is still running. Ends the while 
        #if event.type == pygame.MOUSEBUTTONUP:
        #     print('mouse up')
        
        if game_active:
            if event.type == pygame.KEYDOWN: #Checks for button press
                print('bp')
            if event.type == pygame.KEYUP: #Checks for the abscence of button press
                print('nbp')
        else:
            if event.type == pygame.KEYDOWN  and event.key == pygame.K_SPACE:
                game_active = True
                #mob_rect.x = 20 #temporary
        if event.type == obstacle_timer and game_active:
            obstacle_rect_list.append(mob_surface.get_rect(topleft = (750, randint(0, 630)))) #gets the list and appends something new to it

   #Where the gameplay happens
    if game_active:
            #pygame.MOUSEMOTION: print(event.pos)   checks for mouse movement. display location of the mouse on the image surface
        screen.blit(test_surface,(0,0)) #X goes to the right and Y goes down
       # screen.blit(mob_surface, mob_rect) #replaces the image surface on screen without deleting the previous image. Solved by using convert?
        screen.blit(player_surface, player_rect) #takes the player_surface and puts it in/on top of the rectangle

        #pygame.draw.rect(screen, "#00ff66", coin_rect) #draws a border rect around coin rect and makes it brown (surface, color, shape,line width(optional), ) Leaves middle empty, need to duplicate line" The ultimate introduction to Pygame" 1:20:28
       #pygame.draw.rect(screen, "#F7F7F7", coin_rect, 10)
        #pygame.draw.line(screen, 'Red', (0,0), (700, 630)) draws a line from top left to bottm right. (surface, colour, start position, end position, line width) " The ultimate introduction to Pygame" 1:22:00
    
        #screen.blit(coin_surface,coin_rect)
        
        #mob_x_pos +=7 moves x position by one each time the program loops. Affected by the clock tick rate
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
           player_rect.x += 1
        #mob_rect.left += 1
        #if mob_x_pos < 300: mob_x_pos += 5 else:    mob_x_pos -= 3
        #if mob_rect.x > 700:
           # mob_rect.x = -10
        
        #Obstacle Movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        #Collision
        game_active = collisions(player_rect, obstacle_rect_list)
        #if mob_x_pos > 700:
        #    mob_x_pos = -10 # sends character to other part of the surface when then meet the criteria. Affected by the clock tick rate
        #draw all elements and update everything

        #print(player_rect.colliderect(mob_rect)) display 0 or 1, true or false if the character is colliding with the mob
        #if player_rect.colliderect(mob_rect):
            #print('Collide') triggers multiple times , so have to find a way to prevent it from occuring multiple times
        #mouse_pos = pygame.mouse.get_pos() #gets mouse position during each loop
        #if player_rect. collidepoint(mouse_pos):
         #   print(pygame.mouse.get_pressed()) # checks if the player char has been clicked on by the character and which mouse click the butotn isw''' 
        #if mob_rect.colliderect(player_rect):
            #game_active = False #stops the frame movement when mob hits player
    else: #Could be used for Main menu/death screen
        screen.fill("#3d6396")
        #screen.blit(gameover_surf1,over_rect)
        screen.blit(game_name,name_rect)
        screen.blit(gameover_surf2, over_rect2)
    pygame.display.update()#Constantly updates the window?
    clock.tick(60) # Tells the while loop to not run faster than 60fps

    

''' Blit - Block image transfer
Rects used for precise postioning of surfaces or Basic collisions

Rectangle works based of points " The ultimate introduction to Pygame" 53:02
Tuple (X,Y)
Individual Position

If any of the points , all the other points will be moved along with it.
For precise control over the placement of image variables, make use of both image surface and rectangles
To move things in Pygame, you dont move the surface. Move the Rectangle that moves the surface " The ultimate introduction to Pygame" 59???
collision: rect1.colliderect(rect2) its a boolean statement, so it can only be zero or one
rect1.collidepoint((x,y)) check if one point collides with another. Spcifically good for mouse detection??? " The ultimate introduction to Pygame" 1:07:10
pygame.mouse(mouse position, clicks, buttons, visibility)

if event.type == pygame.MOUSEMOTION
    if player_rect.collidepoint(event.pos):  print('collision')
checks for the mouse movement then checks if the mouse is colliding with player rect based off of its position and prints 'collision'
rects can be used for drawing
pygame.draw: Drawing with multiple shapes or lines

Colours using RGB or Hexadecimal
vscode/python/pygame displays the hexadecimal colours?
CHanging opacity might break something\
pygame.key.get_pressed can be used to see if a Button is being pressed
1:35:30 "The ultimate introduction to Pygame"
pygame.keys and pygame.mouse is good for classes
53:25 "The ultimate introduction to Pygame" FOR RECT POSITIONS
the rect collision tools zooms to fit the entire original image, transparent area or otherwise

Research Global Scope and Local Scope
'''