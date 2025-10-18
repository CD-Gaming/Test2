import pygame
from sys import exit #might not need this is using the boolean method
from random import randint


class Player(pygame.sprite.Sprite):
    def __init__ (self): #initializes sprite class
        super().__init__()
        player_down_1 = pygame.image.load("Sprites/Player/Down_anim/Fatk1.png").convert_alpha()
        player_down_2 = pygame.image.load("Sprites/Player/Down_anim/Fatk2.png").convert_alpha()
        player_down_3 = pygame.image.load("Sprites/Player/Down_anim/Fatk3.png").convert_alpha()
        player_down_4 = pygame.image.load("Sprites/Player/Down_anim/Fatk4.png").convert_alpha()
        player_down_5 = pygame.image.load("Sprites/Player/Down_anim/Fatk5.png").convert_alpha()
        self.player_down = [player_down_1,player_down_2,player_down_3,player_down_4,player_down_5]
        self.player_index = 0

        self.image = self.player_down[self.player_index]
        self.rect = self.image.get_rect(center = (350, 315))


    def player_anim(self):#NESTED IF FOR ATTACKING WHILE FACING A CERTAIN DIRECTION
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            
            self.player_index += 1
            print(self.player_index)
            if self.player_index >= len(self.player_down): self.player_index = 0 #Checks for the number of values in the list then change player index accordinly 
            self.image = self.player_down[int(self.player_index)]
            
    
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
           self.rect.x += 1
    
    def update(self):
        self.player_input()
        self.player_anim()



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

'''def player_animation():
    #decide which animation to play based on the key being pressed
    global player_surf, player_index #2:57:43'''

pygame.init() #initializes
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


player_down_1 = pygame.image.load("Sprites/Player/Down_anim/Fatk1.png").convert_alpha()
player_down_2 = pygame.image.load("Sprites/Player/Down_anim/Fatk2.png").convert_alpha()
player_down_3 = pygame.image.load("Sprites/Player/Down_anim/Fatk3.png").convert_alpha()
player_down_4 = pygame.image.load("Sprites/Player/Down_anim/Fatk4.png").convert_alpha()
player_down_5 = pygame.image.load("Sprites/Player/Down_anim/Fatk5.png").convert_alpha()
player_down = [player_down_1,player_down_2,player_down_3,player_down_4,player_down_5]
player_index = 0
player_surf = player_down[player_index]
player_surf = pygame.transform.scale(player_surf,(player_surf.get_width()*.4, player_surf.get_height()*.4))
player_rect = player_surf.get_rect(center = (350,315)) 

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
        screen.blit(player_surf, player_rect) #takes the player_surface and puts it in/on top of the rectangle
         
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

