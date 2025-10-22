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
        
        self.player_down =  [player_down_1,player_down_2,player_down_3,player_down_4,player_down_5 ]
        self.player_up =    [player_up_1,player_up_2,player_up_3,player_up_4,player_up_5]
        self.player_left =  [player_left_1,player_left_2,player_left_3,player_left_4,player_left_5]
        self.player_right = [player_right_1,player_right_2,player_right_3,player_right_4,player_right_5]

        self.player_index = 0
        self.scale = .8
        self.image = self.player_down[self.player_index]
        self.image = pygame.transform.scale(self.image,(self.image.get_width()*self.scale, self.image.get_height()*self.scale))
        self.rect = self.image.get_rect(center = (350, 340))
        self.anim_speed = .2
        self.move_speed = 2

    def player_anim_Down(self):
        self.player_index += self.anim_speed
        self.rect.y  += self.move_speed
        #print(self.player_index)
        if self.player_index >= len(self.player_down): self.player_index = 0 #Checks for the number of values in the list then change player index accordinly 
        self.image = self.player_down[int(self.player_index)]
        self.image = pygame.transform.scale(self.image,(self.image.get_width()*self.scale, self.image.get_height()*self.scale))
        
    def player_anim_Up(self):      
        self.player_index += self.anim_speed
        self.rect.y  -= self.move_speed 
        #print(self.player_index)
        if self.player_index >= len(self.player_up): self.player_index = 0 
        self.image = self.player_up[int(self.player_index)]  
        self.image = pygame.transform.scale(self.image,(self.image.get_width()*self.scale, self.image.get_height()*self.scale))
    
    def player_anim_Right(self):   
        self.player_index += self.anim_speed
        self.rect.x  += self.move_speed
        #print(self.player_index)
        if self.player_index >= len(self.player_right): self.player_index = 0 
        self.image = self.player_right[int(self.player_index)]
        self.image = pygame.transform.scale(self.image,(self.image.get_width()*self.scale, self.image.get_height()*self.scale))

    def player_anim_Left(self):    
        self.player_index +=self.anim_speed
        self.rect.x  -= self.move_speed
       # print(self.player_index)
        if self.player_index >= len(self.player_left): self.player_index = 0 
        self.image = self.player_left[int(self.player_index)]
        self.image = pygame.transform.scale(self.image,(self.image.get_width()*self.scale, self.image.get_height()*self.scale))
           
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
        #Player_Hitbox()



class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        slime_right_1 = pygame.image.load('Sprites/Slime/Right/Rsv1.png').convert_alpha()
        slime_right_2 = pygame.image.load('Sprites/Slime/Right/Rsv2.png').convert_alpha()
        slime_right_3 = pygame.image.load('Sprites/Slime/Right/Rsv3.png').convert_alpha()
        slime_right_4 = pygame.image.load('Sprites/Slime/Right/Rsv4.png').convert_alpha()
        slime_right_5 = pygame.image.load('Sprites/Slime/Right/Rsv5.png').convert_alpha()
        slime_right_6 = pygame.image.load('Sprites/Slime/Right/Rsv6.png').convert_alpha()
        
        slime_left_1 = pygame.image.load('Sprites/Slime/Left/SSV 1.png').convert_alpha()
        slime_left_2 = pygame.image.load('Sprites/Slime/Left/SSV 2.png').convert_alpha()
        slime_left_3 = pygame.image.load('Sprites/Slime/Left/SSV 3.png').convert_alpha()
        slime_left_4 = pygame.image.load('Sprites/Slime/Left/SSV 4.png').convert_alpha()
        slime_left_5 = pygame.image.load('Sprites/Slime/Left/SSV 5.png').convert_alpha()
        slime_left_6 = pygame.image.load('Sprites/Slime/Left/SSV 6.png').convert_alpha()
        
        slime_up_1 = pygame.image.load('Sprites/Slime/Front/SFV 1.png').convert_alpha()
        slime_up_2 = pygame.image.load('Sprites/Slime/Front/SFV 2.png').convert_alpha()
        slime_up_3 = pygame.image.load('Sprites/Slime/Front/SFV 3.png').convert_alpha()
        slime_up_4 = pygame.image.load('Sprites/Slime/Front/SFV 4.png').convert_alpha()
        slime_up_5 = pygame.image.load('Sprites/Slime/Front/SFV 5.png').convert_alpha()
        slime_up_6 = pygame.image.load('Sprites/Slime/Front/Ssv6.png').convert_alpha()

        slime_down_1 = pygame.image.load('Sprites/Slime/Back/SBV 1.png').convert_alpha()
        slime_down_2 = pygame.image.load('Sprites/Slime/Back/SBV 2.png').convert_alpha()
        slime_down_3 = pygame.image.load('Sprites/Slime/Back/SBV 3.png').convert_alpha()
        slime_down_4 = pygame.image.load('Sprites/Slime/Back/SBV 4.png').convert_alpha()
        slime_down_5 = pygame.image.load('Sprites/Slime/Back/SBV 5.png').convert_alpha()
        slime_down_6 = pygame.image.load('Sprites/Slime/Back/SBV 6.png').convert_alpha()
        
        self.slime_right =  [slime_right_1,slime_right_2, slime_right_3, slime_right_4, slime_right_5, slime_right_6]
        self.slime_left =   [slime_left_1, slime_left_2, slime_left_3, slime_left_4, slime_left_5, slime_left_6]
        self.slime_up =     [slime_up_1, slime_up_2, slime_up_3, slime_up_4, slime_up_5, slime_up_6]
        self.slime_down =   [slime_down_1, slime_down_2, slime_down_3, slime_down_4, slime_down_5, slime_down_6]
        self.enemy_index = 0
        self.image = self.slime_right[self.enemy_index]
        
       
        self.rect = self.image.get_rect(center = (775, randint(300, 500)))
        self.image = pygame.transform.scale(self.image,(self.image.get_width()*.2, self.image.get_height()*.2))
        self.anim_speed = .15
        self.move_speed = 2
        self.enemy_timer = 0

    #def y_target(self):
     #   if self.rect.y > 315:
      #          self.rect.y -= self.move_speed
       # elif self.rect.y < 315:
        #        self.rect.y += self.move_speed
    
    def spawn_timer(self):
        while self.enemy_timer <= 60000:  
            enemy_timer += 1 #to spawn from the other sides

    

    def slime_anim_right (self):
        self.enemy_index += self.anim_speed
        self.rect.x  -= self.move_speed 
        if self.enemy_index >= len(self.slime_right): self.enemy_index = 0
        self.image = self.slime_right[int(self.enemy_index)]
        self.image = pygame.transform.scale(self.image,(self.image.get_width()*.2, self.image.get_height()*.2))
        #self.y_target()

    def slime_anim_left (self):
        self.enemy_index += self.anim_speed
        self.rect.x  += self.move_speed 
        if self.enemy_index >= len(self.slime_left): self.enemy_index = 0
        self.image = self.slime_left[int(self.enemy_index)]
        self.image = pygame.transform.scale(self.image,(self.image.get_width()*.2, self.image.get_height()*.2))
        #self.y_target()


    
    def update(self):
        self.slime_anim_right()
        #Enemy_Hitbox()
        #self.destroy()

    def destroy(self):
       # if self.rect.x == 350 :#and self.rect.y == 0:
           self.kill() #destroys enemy sprite
      #  elif 



class Player_Hitbox(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        hbox = pygame.image.load("Hitbox.png").convert_alpha()
        #self.hitbox = pygame.draw.rect(screen,"#eb4c4cff", (326, 275, 45,45),5)
        self.image = hbox
        self.image = pygame.transform.scale(self.image,(self.image.get_width()*.4, self.image.get_height()*.4))
        self.rect = self.image.get_rect(center = (350,310))
        self.move_speed = 2
        
    
    def hbox_direction(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
           self.rect.y += self.move_speed
        if keys[pygame.K_UP]:
           self.rect.y -= self.move_speed
        if keys[pygame.K_RIGHT]:
           self.rect.x += self.move_speed
        if keys[pygame.K_LEFT]:
           self.rect.x -= self.move_speed
    def r(self):
        #if game_active == False:
                   self.rect = self.image.get_rect(center = (350,310))
            
        

    def update(self):
        
        self.hbox_direction()
       # self.r() 
        
def collision_sprite():
    if  pygame.sprite.spritecollide(p_hitbox.sprite,enemy_group,False):
        enemy_group.empty()
       # p_hitbox.update()
       # p_hitbox.r()
        return False
    else:
        return True
    

    
screen = pygame.display.set_mode((700,630))
pygame.display.set_caption('Slime Survivor') #Chanes title of window





clock = pygame.time.Clock() #To deal with time and framerate?
bg_music = pygame.mixer.Sound('Sound/bass.wav')
bg_music.play(loops = -1) #sets the music to loop infinetly
#Groups
enemy_group = pygame.sprite.Group()
e_hitbox = pygame.sprite.Group()

player = pygame.sprite.GroupSingle()
player.add(Player()) #puts an instance of the Player class into a group single
p_hitbox = pygame.sprite.GroupSingle()
p_hitbox.add(Player_Hitbox())



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
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit() 
            exit()

        if game_active:
            if event.type == pygame.KEYDOWN: 
                print('bp')
            if event.type == pygame.KEYUP: 
                print('nbp')
        else:
            if event.type == pygame.KEYDOWN  and event.key == pygame.K_SPACE:
                game_active = True
                
        if game_active:
            if event.type == obstacle_timer:
                enemy_group.add(Enemy())
                
   
    if game_active:
        screen.blit(test_surface,(0,0))
           
        #Player
        player.draw(screen)
        player.update()

        #Obstacle Movement
        enemy_group.draw(screen)
        e_hitbox.draw(screen)
        enemy_group.update()
        

        #Hitbox
        p_hitbox.draw(screen)
        p_hitbox.update()
        
        #Collision
        game_active = collision_sprite() 
       
        
       
    else: 
        
       
        screen.fill("#3d6496")
        
        screen.blit(game_name,name_rect)
        screen.blit(gameover_surf2, over_rect2)
       
    pygame.display.update()
    clock.tick(60)

  
