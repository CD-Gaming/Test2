import pygame
from sys import exit #might not need this is using the boolean method
from random import randint
pygame.init() #initializes

class Player(pygame.sprite.Sprite):
    def __init__ (self): #initializes sprite class
        super().__init__()
        self.image = pygame.image.load("Sprites/SwordSp1.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom = (350, 315))
    
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
           self.rect.x += 1
    
    def update(self):
        self.player_input()

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 2

            screen.blit(mob_surface,obstacle_rect)
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        return obstacle_list
    else: return []

def collisions(player,obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect): return False 
    return True

screen = pygame.display.set_mode((700,630))
pygame.display.set_caption('Slime Slayer') #Chanes title of window
clock = pygame.time.Clock() #To deal with time and framerate?

player = pygame.sprite.GroupSingle()
player.add(Player()) #puts an instance of the Player class into a group single

#Text
font = pygame.font.Font('Font.ttf', 60)
s_font = pygame.font.Font('Font.ttf', 20)

test_surface = pygame.image.load('background.png').convert()
test_surface = pygame.transform.scale(test_surface,(test_surface.get_width()*.7, test_surface.get_height()*.7))

game_active = False

#Obstacle
mob_surface = pygame.image.load('Sprites/Slime/Side/Slime.png').convert_alpha()
mob_surface = pygame.transform.scale(mob_surface,(mob_surface.get_width()*.3, mob_surface.get_height()*.3))

obstacle_rect_list = []

#Text
gameover_surf2 = s_font.render('Press [Spacebar] to start', False,'White')
over_rect2 = gameover_surf2.get_rect(center = (360, 400))
game_name = font.render('Slime Slayer', False, 'White')
name_rect = game_name.get_rect(midtop = (360, 100))


player_surface = pygame.image.load("Sprites/SwordSp1.png").convert_alpha()
player_surface = pygame.transform.scale(player_surface,(player_surface.get_width()*.4, player_surface.get_height()*.4))
player_rect = player_surface.get_rect(center = (350,315)) 

#Timer
obstacle_timer = pygame.USEREVENT + 1 #+1 is to avoid the preset events in pygame
pygame.time.set_timer(obstacle_timer, 500) #triggers event and determines how often the even should be triggered. Triggers event every 1000 milli seconds (1second)

while True:
    for event in pygame.event.get(): #check through "event"s based what event was update from the "get()" function
        if event.type == pygame.QUIT: #meaning if the x button is 
            pygame.quit() #closes the game. Uninitializes, causes an error by itself
            exit() #ends any code that is still running. Ends the while 
        
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
          
        screen.blit(test_surface,(0,0)) #X goes to the right and Y goes down
       
        
        
        #Player
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
           player_rect.x += 1
        screen.blit(player_surface, player_rect) #takes the player_surface and puts it in/on top of the rectangle
        player.draw(screen)
        player.update()
        
        #Obstacle Movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        #Collision
        game_active = collisions(player_rect, obstacle_rect_list)
       
    else: #Could be used for Main menu/death screen
        obstacle_rect_list.clear() #deletes rects when game is not running
        player_rect.center = (350,315) #resets player character to this position
        screen.fill("#3d6396")
        #screen.blit(gameover_surf1,over_rect)
        screen.blit(game_name,name_rect)
        screen.blit(gameover_surf2, over_rect2)
    pygame.display.update()#Constantly updates the window?
    clock.tick(60) # Tells the while loop to not run faster than 60fps

    '''Functions of the Sprite Class,
        draw()
        update()
    '''

