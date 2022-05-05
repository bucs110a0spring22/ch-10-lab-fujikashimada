import pygame
import random

#model
class Enemy(pygame.sprite.Sprite):
    def __init__(self, name, x, y, img_file):
        #initialize all the Sprite functionality
        pygame.sprite.Sprite.__init__(self)

        #The following two attributes must be called image and rect
        #pygame assumes you have intitialized these values
        #and uses them to update the screen

        #create surface object image
        self.image = pygame.image.load(img_file).convert_alpha()
        #get the rectangle for positioning
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        #set other attributes
        self.name = name + str(id(self))
        self.speed = 2
        

    def update(self, speed=2, x=0, y=0):
      '''
      part A randomly moves enemy, part B moves enemy towards the hero. 
      args: (int) input position and speed
      return: causes it to move randomly or towards the hero. 
      '''
      #part A 
      #self.rect.x = random.randrange(-2, 1)
      #self.rect.y = random.randrange(-2, 1)

      #part B
      #movement along the x 
      if self.rect.x >= x:
        self.rect.x -= self.speed
      elif self.rect.x < x:
        self.rect.x += self.speed
      #movement along the y 
      if self.rect.y >= y:
        self.rect.y -= self.speed
      elif self.rect.y < y:
        self.rect.y += self.speed
        
      print("'Update me,' says " + self.name)

        
