import pygame
from sys import exit #might not need this is using the boolean method
pygame.init() #initializes

screen = pygame.display.set_mode((700,630))
pygame.display.set_caption('Untitled') #Chanes title of window
clock = pygame.time.Clock() #To deal with time and framerate?

font = pygame.font.Font('Font.ttf', 25)

test_surface = pygame.image.load('background.png').convert()
test_surface = pygame.transform.scale(test_surface,(test_surface.get_width()*.7, test_surface.get_height()*.7))


mob_surface = pygame.image.load('Sprites/Slime/Side/SlimeSV.png').convert_alpha()
mob_surface = pygame.transform.scale(mob_surface,(mob_surface.get_width()*.3, mob_surface.get_height()*.3))

coin_surface = font.render('$0', False, (214, 209, 69))
coin_rect = coin_surface.get_rect(topleft = (50, 15))
mob_x_pos = 30
mob_rect = mob_surface.get_rect(topleft = (mob_x_pos,200))


player_surface = pygame.image.load("Sprites\SwordSp1.png").convert_alpha()
player_surface = pygame.transform.scale(player_surface,(player_surface.get_width()*.4, player_surface.get_height()*.4))
player_rect = player_surface.get_rect(topright = (100,175)) #pygame.Rect(left, top, width, height). getRect(gets the size of the variable/object)
#get_rect(area,(x,y)) The area changes the center of which the rect is moved. For example from center to middle bottom can be used to place image surfaces on the ground " The ultimate introduction to Pygame" 57:55

#test_surface = pygame.Surface((100,200)) 'Surface' must be capitalized
#test_surface.fill("Blue") sets the surface colour to blue

while True:
    for event in pygame.event.get(): #check through "event"s based what event was update from the "get()" function
        if event.type == pygame.QUIT: #meaning if the x button is 
            pygame.quit() #closes the game. Uninitializes, causes an error by itself
            exit() #ends any code that is still running. Ends the while 
        if event.type == pygame.MOUSEBUTTONUP:
            print('mouse up')
        #pygame.MOUSEMOTION: print(event.pos)   checks for mouse movement. display location of the mouse on the image surface
    screen.blit(test_surface,(0,0)) #X goes to the right and Y goes down
    screen.blit(mob_surface, mob_rect) #replaces the image surface on screen without deleting the previous image. Solved by using convert?
    screen.blit(player_surface, player_rect) #takes the player_surface and puts it in/on top of the rectangle

    pygame.draw.rect(screen, "#00ff66", coin_rect) #draws a border rect around coin rect and makes it brown (surface, color, shape,line width(optional), ) Leaves middle empty, need to duplicate line" The ultimate introduction to Pygame" 1:20:28
    pygame.draw.rect(screen, "#F7F7F7", coin_rect, 10)
    #pygame.draw.line(screen, 'Red', (0,0), (700, 630)) draws a line from top left to bottm right. (surface, colour, start position, end position, line width) " The ultimate introduction to Pygame" 1:22:00
   
    screen.blit(coin_surface,coin_rect)
    
    #mob_x_pos +=7 moves x position by one each time the program loops. Affected by the clock tick rate
    
    #mob_rect.left += 1
    #if mob_x_pos < 300: mob_x_pos += 5 else:    mob_x_pos -= 3
    if mob_rect.x > 700:
        mob_rect.x = -10
    
    #if mob_x_pos > 700:
    #    mob_x_pos = -10 # sends character to other part of the surface when then meet the criteria. Affected by the clock tick rate
    #draw all elements and update everything

    '''print(player_rect.colliderect(mob_rect)) display 0 or 1, true or false if the character is colliding with the mob
    if player_rect.colliderect(mob_rect):
        #print('Collide') triggers multiple times , so have to find a way to prevent it from occuring multiple times
    mouse_pos = pygame.mouse.get_pos() #gets mouse position during each loop
    if player_rect. collidepoint(mouse_pos):
        print(pygame.mouse.get_pressed()) # checks if the player char has been clicked on by the character and which mouse click the butotn isw''' 
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
'''