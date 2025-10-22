import pygame
from sys import exit #might not need this is using the boolean method
from random import randint
pygame.init() #initializes 


class Player(pygame.sprite.Sprite):
    def __init__ (self): #initializes sprite class
        super().__init__()
        player_down_1 = pygame.image.load("Sprites/Player/Down1.png").convert_alpha()
        player_down_2 = pygame.image.load("Sprites/Player/Down2.png").convert_alpha()
        player_down_3 = pygame.image.load("Sprites/Player/Down3.png").convert_alpha()
        

        player_up_1 = pygame.image.load("Sprites/Player/Up1.png").convert_alpha()
        player_up_2 = pygame.image.load("Sprites/Player/Up2.png").convert_alpha()
        player_up_3 = pygame.image.load("Sprites/Player/Up3.png").convert_alpha()
        
        player_left_1 = pygame.image.load("Sprites/Player/Left1.png").convert_alpha()
        player_left_2 = pygame.image.load("Sprites/Player/Left2.png").convert_alpha()
        player_left_3 = pygame.image.load("Sprites/Player/Left3.png").convert_alpha()

        player_right_1 = pygame.image.load("Sprites/Player/Right1.png").convert_alpha()
        player_right_2 = pygame.image.load("Sprites/Player/Right2.png").convert_alpha()
        player_right_3 = pygame.image.load("Sprites/Player/Right3.png").convert_alpha()
        
        self.player_down =  [player_down_1,player_down_2,player_down_3 ]
        self.player_up =    [player_up_1,player_up_2,player_up_3]
        self.player_left =  [player_left_1,player_left_2,player_left_3]
        self.player_right = [player_right_1,player_right_2,player_right_3]
        self.player_index = 0
        self.scale = .8
        self.image = self.player_down[self.player_index]
        self.image = pygame.transform.scale(self.image,(self.image.get_width()*self.scale, self.image.get_height()*self.scale))
        self.rect = self.image.get_rect(center = (350, 340))
        self.anim_speed = .2
        self.move_speed = 2
        self.walk_sound = pygame.mixer.Sound('Sound/Grass_step.wav')

    def player_anim_Down(self):
        if self.rect.y >= 480:
            self.rect.y = 478  
        self.player_index += self.anim_speed
        self.rect.y  += self.move_speed
        #print(self.player_index)
        if self.player_index >= len(self.player_down): self.player_index = 0 #Checks for the number of values in the list then change player index accordinly 
        self.image = self.player_down[int(self.player_index)]
        self.image = pygame.transform.scale(self.image,(self.image.get_width()*self.scale, self.image.get_height()*self.scale))
        
    def player_anim_Up(self):     
        if self.rect.y <= -2:
            self.rect.y = 0  
        self.player_index += self.anim_speed
        self.rect.y  -= self.move_speed 
        #print(self.player_index)
        if self.player_index >= len(self.player_up): self.player_index = 0 
        self.image = self.player_up[int(self.player_index)]  
        self.image = pygame.transform.scale(self.image,(self.image.get_width()*self.scale, self.image.get_height()*self.scale))
    
    def player_anim_Right(self):   
        if self.rect.x >= 630:
            self.rect.x = 628   
        self.player_index += self.anim_speed
        self.rect.x  += self.move_speed
        #print(self.player_index)
        if self.player_index >= len(self.player_right): self.player_index = 0 
        self.image = self.player_right[int(self.player_index)]
        self.image = pygame.transform.scale(self.image,(self.image.get_width()*self.scale, self.image.get_height()*self.scale))

    def player_anim_Left(self): 
        if self.rect.x <= -2:
            self.rect.x = 0   
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
           # self.walk_sound.play(loops = 1)
           
        if keys[pygame.K_UP]:
            self.player_anim_Up()

        if keys[pygame.K_RIGHT]:
            self.player_anim_Right()
               
        if keys[pygame.K_LEFT]:
            self.player_anim_Left()
            
    def update(self):
        self.player_input()
        if game_active == False:
            self.image = self.player_down[0]

            self.image = pygame.transform.scale(self.image,(self.image.get_width()*self.scale, self.image.get_height()*self.scale))

            self.rect = self.image.get_rect(center = (350, 340))

class Enemy_right(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.anim_speed = .05
        self.move_speed = 2
        self.enemy_timer = 0
        self.enemy_size = .35

        slime_right_1 = pygame.image.load('Sprites/Slime/Right1.png').convert_alpha()
        slime_right_2 = pygame.image.load('Sprites/Slime/Right2.png').convert_alpha()
        
        self.slime_right =  [slime_right_1,slime_right_2]
        
        self.enemy_index = 0
        self.image = self.slime_right[self.enemy_index]
        self.image = pygame.transform.scale(self.image,(self.image.get_width()*self.enemy_size, self.image.get_height()*self.enemy_size))
        self.rect = self.image.get_rect(center = (-20, randint(200, 500)))

    

    def slime_anim_right (self):
       
        self.enemy_index += self.anim_speed
        self.rect.x  += self.move_speed 
        if self.enemy_index >= len(self.slime_right): self.enemy_index = 0
        self.image = self.slime_right[int(self.enemy_index)]
        self.image = pygame.transform.scale(self.image,(self.image.get_width()*self.enemy_size, self.image.get_height()*self.enemy_size))
        #self.y_target()
    
    def update(self):
        self.slime_anim_right()
        
        self.destroy()

    def destroy(self):
        if self.rect.x == 650:#and self.rect.y == 0:
           self.kill() #destroys enemy sprite
      #  elif 
        if game_active == False:
            self.kill()

class Enemy_left(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.anim_speed = .05
        self.move_speed = 2
        self.enemy_timer = 0
        self.enemy_size = .35


        
        slime_left_1 = pygame.image.load('Sprites/Slime/Left1.png').convert_alpha()
        slime_left_2 = pygame.image.load('Sprites/Slime/Left2.png').convert_alpha()
        
  
        
        
        self.slime_left =   [slime_left_1, slime_left_2]
       
        self.enemy_index = 0
        self.image = self.slime_left[self.enemy_index]
        self.image = pygame.transform.scale(self.image,(self.image.get_width()*self.enemy_size, self.image.get_height()*self.enemy_size))
       
        self.rect = self.image.get_rect(center = (775, randint(200, 500)))

    def slime_anim_left (self):
        
        self.enemy_index += self.anim_speed
        self.rect.x  -= self.move_speed 
        if self.enemy_index >= len(self.slime_left): self.enemy_index = 0
        self.image = self.slime_left[int(self.enemy_index)]
        self.image = pygame.transform.scale(self.image,(self.image.get_width()*self.enemy_size, self.image.get_height()*self.enemy_size))
        #self.y_target()
    
    def update(self):
        self.slime_anim_left()
        
        self.destroy()

    def destroy(self):
        if self.rect.x == 0:#and self.rect.y == 0:
           self.kill() #destroys enemy sprite
        if game_active == False:
            self.kill()
            
class Enemy_up(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.anim_speed = .05
        self.move_speed = 2
        self.enemy_timer = 0
        self.enemy_size = .35
        
        slime_up_1 = pygame.image.load('Sprites/Slime/Up1.png').convert_alpha()
        slime_up_2 = pygame.image.load('Sprites/Slime/Up2.png').convert_alpha()

        self.slime_up =     [slime_up_1, slime_up_2]
     
        self.enemy_index = 0
        self.image = self.slime_up[self.enemy_index]
        self.image = pygame.transform.scale(self.image,(self.image.get_width()*self.enemy_size, self.image.get_height()*self.enemy_size))
        self.rect = self.image.get_rect(center = (randint(100, 600), 790))
    
    def spawn_timer(self):
        while self.enemy_timer <= 30000:  
            enemy_timer += 1 #to spawn from the other sides

    def slime_anim_up (self):
        
        self.enemy_index += self.anim_speed
        self.rect.y  -= self.move_speed 
        if self.enemy_index >= len(self.slime_up): self.enemy_index = 0
        self.image = self.slime_up[int(self.enemy_index)]
        self.image = pygame.transform.scale(self.image,(self.image.get_width()*self.enemy_size, self.image.get_height()*self.enemy_size))
        
    def update(self):
        self.slime_anim_up()
        
        self.destroy()

    def destroy(self):
        if self.rect.y == 0:#and self.rect.y == 0:
           self.kill() #destroys enemy sprite
        if game_active == False:
            self.kill()

class Enemy_down(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.anim_speed = .05
        self.move_speed = 2
        self.enemy_timer = 0
        self.enemy_size = .35

        slime_down_1 = pygame.image.load('Sprites/Slime/Down1.png').convert_alpha()
        slime_down_2 = pygame.image.load('Sprites/Slime/Down2.png').convert_alpha()
        
        
        self.slime_down =   [slime_down_1, slime_down_2]
        self.enemy_index = 0
        self.image = self.slime_down[self.enemy_index]
        self.image = pygame.transform.scale(self.image,(self.image.get_width()*self.enemy_size, self.image.get_height()*self.enemy_size))
        self.rect = self.image.get_rect(center = (randint(100, 600), 0))
    
    def spawn_timer(self):
        while self.enemy_timer <= 45000:  
            enemy_timer += 1 #to spawn from the other sides

    def slime_anim_down (self):
        
        self.enemy_index += self.anim_speed
        self.rect.y  += self.move_speed 
        if self.enemy_index >= len(self.slime_down): self.enemy_index = 0
        self.image = self.slime_down[int(self.enemy_index)]
        self.image = pygame.transform.scale(self.image,(self.image.get_width()*self.enemy_size, self.image.get_height()*self.enemy_size))
        
    
    def update(self):
        self.slime_anim_down()
        
        self.destroy()

    def destroy(self):
        if self.rect.y == 790:#and self.rect.y == 0:
           self.kill() #destroys enemy sprite
        if game_active == False:
            self.kill()
        
def collision_sprite():
    if  pygame.sprite.spritecollide(player.sprite,enemy_group,False):
        enemy_group.empty()
        
     
        return False
    else:
        return True   
         
def collision_sprite2():
    if  pygame.sprite.spritecollide(player.sprite,enemy_group2,False):
        enemy_group2.empty()
        
        return False
    else:
        return True      
      
def collision_sprite3():
    if  pygame.sprite.spritecollide(player.sprite,enemy_group3,False):
        enemy_group3.empty()
     
        return False
    else:
        return True        
 
def collision_sprite4():
    if  pygame.sprite.spritecollide(player.sprite,enemy_group4,False):
        enemy_group4.empty()
     
        return False
    else:
        return True
    

def display_score():
    current_time = int(pygame.time.get_ticks()/1000)  - start_time
    score_surf = s_font.render(f'Score: {current_time}', False,"#083b02")
    score_rect = score_surf.get_rect(center = (350, 500))
    screen.blit(score_surf, score_rect)
    return current_time
   
screen = pygame.display.set_mode((700,630))
pygame.display.set_caption('Slime Survivor') 

clock = pygame.time.Clock() 
bg_music = pygame.mixer.Sound('Sound/bass.wav')
bg_music.play(loops = -1)
start_time = 0
score = 0
h_score = 0

count = 0
enemy_group = pygame.sprite.Group()
enemy_group2 = pygame.sprite.Group()
enemy_group3 = pygame.sprite.Group()
enemy_group4 = pygame.sprite.Group()


player = pygame.sprite.GroupSingle()
player.add(Player()) 


font = pygame.font.Font('Font.ttf', 50)
s_font = pygame.font.Font('Font.ttf', 20)

test_surface = pygame.image.load('background.png').convert()
test_surface = pygame.transform.scale(test_surface,(test_surface.get_width()*.7, test_surface.get_height()*.7))

game_active = False


obstacle_rect_list = []


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
                start_time = int(pygame.time.get_ticks()/ 1000)
                
        if game_active:
            #ENEMY SPAWN TIMER
            if event.type == obstacle_timer:
                
            
                enemy_group.add(Enemy_left())
            if event.type == obstacle_timer and count >= 500:
                
                enemy_group2.add(Enemy_right())
            if event.type == obstacle_timer and count >= 1000:
                
                enemy_group3.add(Enemy_up()) 
            if event.type == obstacle_timer and count >= 2000:
                
                enemy_group3.add(Enemy_right())
               
           
   
    if game_active:
        screen.blit(test_surface,(0,0))
        count += 1
        score = display_score()
        #Player
        player.draw(screen)
        player.update()

        #Obstacle Movement
        enemy_group.draw(screen)
        enemy_group2.draw(screen)
        enemy_group3.draw(screen)
        enemy_group4.draw(screen)
       
        enemy_group.update()
        enemy_group2.update()
        enemy_group3.update()
        enemy_group4.update()
        

       
        #Collision
        if collision_sprite() == False:
            game_active = False
        elif collision_sprite2() == False:
            game_active = False
        elif collision_sprite3() == False:
            game_active = False
        elif collision_sprite4() == False:
            game_active = False
        
       
        
       
    else: 
        player.update()
        enemy_group.empty()
        enemy_group2.empty()
        enemy_group3.empty()
        enemy_group4.empty()
        count = 0
       
        screen.fill("#3d6496")
        
       

        screen.blit(game_name,name_rect)
        screen.blit(gameover_surf2, over_rect2)
        
       
        if score >= h_score:
            h_score = score
        end_score = s_font.render(f'Your current score: {score}', False , "#083b02")
        end_score_rect = end_score.get_rect(center = (350, 500))
        
        high_score_text = s_font.render(f'Highest score:{h_score}', False, "#4ae739")
        high_score_text_rect = high_score_text.get_rect(center = (350, 600))

        if score > 0:
            screen.blit(end_score, end_score_rect)
            screen.blit(high_score_text, high_score_text_rect)
       
    pygame.display.update()
    clock.tick(60)

  
