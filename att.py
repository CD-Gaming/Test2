import pygame
from sys import exit #might not need this is using the boolean method
from random import randint
pygame.init() #initializes 


class Player(pygame.sprite.Sprite):
    def __init__ (self): #initializes sprite class
        super().__init__()
        player_down_1 = pygame.image.load("Sprites/Player/Down_anim/Fatk1.png").convert_alpha()
        player_down_2 = pygame.image.load("Sprites/Player/Down_anim/Fatk2.png").convert_alpha()
        player_down_3 = pygame.image.load("Sprites/Player/Down_anim/Fatk3.png").convert_alpha()
        player_down_4 = pygame.image.load("Sprites/Player/Down_anim/Fatk4.png").convert_alpha()
        player_down_5 = pygame.image.load("Sprites/Player/Down_anim/Fatk5.png").convert_alpha()

        player_up_1 = pygame.image.load("Sprites/Player/Up_anim/Tatk1.png").convert_alpha()
        player_up_2 = pygame.image.load("Sprites/Player/Up_anim/Tatk2.png").convert_alpha()
        player_up_3 = pygame.image.load("Sprites/Player/Up_anim/Tatk3.png").convert_alpha()
        player_up_4 = pygame.image.load("Sprites/Player/Up_anim/Tatk4.png").convert_alpha()
        player_up_5 = pygame.image.load("Sprites/Player/Up_anim/Tatk5.png").convert_alpha()

        player_left_1 = pygame.image.load("Sprites/Player/Left_anim/Latk1.png").convert_alpha()
        player_left_2 = pygame.image.load("Sprites/Player/Left_anim/Latk2.png").convert_alpha()
        player_left_3 = pygame.image.load("Sprites/Player/Left_anim/Latk3.png").convert_alpha()
        player_left_4 = pygame.image.load("Sprites/Player/Left_anim/Latk4.png").convert_alpha()
        player_left_5 = pygame.image.load("Sprites/Player/Left_anim/Latk5.png").convert_alpha()

        player_right_1 = pygame.image.load("Sprites/Player/Right_anim/Ratk1.png").convert_alpha()
        player_right_2 = pygame.image.load("Sprites/Player/Right_anim/Ratk2.png").convert_alpha()
        player_right_3 = pygame.image.load("Sprites/Player/Right_anim/Ratk3.png").convert_alpha()
        player_right_4 = pygame.image.load("Sprites/Player/Right_anim/Ratk4.png").convert_alpha()
        player_right_5 = pygame.image.load("Sprites/Player/Right_anim/Ratk5.png").convert_alpha()
        
        self.player_down = [player_down_1,player_down_2,player_down_3,player_down_4,player_down_5 ]
        self.player_up =  [player_up_1,player_up_2,player_up_3,player_up_4,player_up_5]
        self.player_left = [player_left_1,player_left_2,player_left_3,player_left_4,player_left_5]
        self.player_right =[player_right_1,player_right_2,player_right_3,player_right_4,player_right_5]

        self.player_index = 0
       
        self.image = self.player_down[self.player_index]
        self.image = pygame.transform.scale(self.image,(self.image.get_width()*.6, self.image.get_height()*.6))
        self.rect = self.image.get_rect(center = (350, 315))
        self.anim_speed = .2

    def player_anim_Down(self):
      
        
        self.player_index += self.anim_speed
        #print(self.player_index)
        if self.player_index >= len(self.player_down): self.player_index = 0 #Checks for the number of values in the list then change player index accordinly 
        self.image = self.player_down[int(self.player_index)]
        self.image = pygame.transform.scale(self.image,(self.image.get_width()*.6, self.image.get_height()*.6))
        
    def player_anim_Up(self):      
        
        self.player_index += self.anim_speed
        #print(self.player_index)
        if self.player_index >= len(self.player_up): self.player_index = 0 
        self.image = self.player_up[int(self.player_index)]  
        self.image = pygame.transform.scale(self.image,(self.image.get_width()*.6, self.image.get_height()*.6))
    
    def player_anim_Right(self):   
          
        self.player_index += self.anim_speed
        #print(self.player_index)
        if self.player_index >= len(self.player_right): self.player_index = 0 
        self.image = self.player_right[int(self.player_index)]
        self.image = pygame.transform.scale(self.image,(self.image.get_width()*.6, self.image.get_height()*.6))

    def player_anim_Left(self):    
        
        self.player_index +=self.anim_speed
       # print(self.player_index)
        if self.player_index >= len(self.player_left): self.player_index = 0 
        self.image = self.player_left[int(self.player_index)]
        self.image = pygame.transform.scale(self.image,(self.image.get_width()*.6, self.image.get_height()*.6))
           
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
           self.player_anim_Down()
        if keys[pygame.K_UP]:
           self.player_anim_Up()
        if keys[pygame.K_RIGHT]:
           self.player_anim_Right()
        if keys[pygame.K_LEFT]:
           self.player_anim_Left()
           
    def update(self):
        self.player_input()
        
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        slime_right_1 = pygame.image.load('Sprites/Slime/Right/Rsv1.png').convert_alpha()
        slime_right_2 = pygame.image.load('Sprites/Slime/Right/Rsv2.png').convert_alpha()
        slime_right_3 = pygame.image.load('Sprites/Slime/Right/Rsv3.png').convert_alpha()
        slime_right_4 = pygame.image.load('Sprites/Slime/Right/Rsv4.png').convert_alpha()
        slime_right_5 = pygame.image.load('Sprites/Slime/Right/Rsv5.png').convert_alpha()
        slime_right_6 = pygame.image.load('Sprites/Slime/Right/Rsv6.png').convert_alpha()
        
        self.slime_right = [slime_right_1,slime_right_2, slime_right_3, slime_right_4, slime_right_5, slime_right_6]
        self.enemy_index = 0
        self.image = self.slime_right[self.enemy_index]
        
       
        self.rect = self.image.get_rect(center = (800, randint(300, 500)))
        self.image = pygame.transform.scale(self.image,(self.image.get_width()*.2, self.image.get_height()*.2))
        self.anim_speed = .15
        self.move_speed = 2
   
    def slime_anim_right (self):
        self.enemy_index += self.anim_speed
        self.rect.x  -= self.move_speed 
        if self.enemy_index >= len(self.slime_right): self.enemy_index = 0
        self.image = self.slime_right[int(self.enemy_index)]
        self.image = pygame.transform.scale(self.image,(self.image.get_width()*.2, self.image.get_height()*.2))
    
    def update(self):
        self.slime_anim_right()
       # self.destroy()

    def destroy(self):
        if self.rect.x == 350 :#and self.rect.y == 0:
            self.kill() #destroys enemy sprite
      #  elif 
        

def collision_sprite():
    if  pygame.sprite.spritecollide(player.sprite,enemy_group,False):
        enemy_group.empty()
        return False
    else:
        return True




screen = pygame.display.set_mode((700,630))
pygame.display.set_caption('Slime Survivor') #Chanes title of window
clock = pygame.time.Clock() #To deal with time and framerate?
#Groups
enemy_group = pygame.sprite.Group()

player = pygame.sprite.GroupSingle()
player.add(Player()) #puts an instance of the Player class into a group single

#Text
font = pygame.font.Font('Font.ttf', 50)
s_font = pygame.font.Font('Font.ttf', 20)

test_surface = pygame.image.load('background.png').convert()
test_surface = pygame.transform.scale(test_surface,(test_surface.get_width()*.7, test_surface.get_height()*.7))

game_active = False


obstacle_rect_list = []

#Text
gameover_surf2 = s_font.render('Press [Spacebar] to start', False,'White')
over_rect2 = gameover_surf2.get_rect(center = (360, 400))
game_name = font.render('Slime Survivor', False, 'White')
name_rect = game_name.get_rect(midtop = (360, 100))




#Timer
obstacle_timer = pygame.USEREVENT + 1 #+1 is to avoid the preset events in pygame
pygame.time.set_timer(obstacle_timer, 2500) #triggers event and determines how often the even should be triggered. Triggers event every 1000 milli seconds (1second)

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
        if game_active:
            if event.type == obstacle_timer:
                enemy_group.add(Enemy())
                
   #Where the gameplay happens
    if game_active:
        screen.blit(test_surface,(0,0)) #X goes to the right and Y goes down
               
        #Player
        player.draw(screen)
        player.update()

        #Obstacle Movement
        enemy_group.draw(screen)
        enemy_group.update()

        
        #Collision
        game_active = collision_sprite()
       
    else: #Could be used for Main menu/death screen
        obstacle_rect_list.clear() #deletes rects when game is not running
       # player_rect.center = (350,315) #resets player character to this position
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

