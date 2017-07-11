import pygame
import random
import math
width = 1600
height = 1600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Fern')
clock = pygame.time.Clock()
screen.fill((255,255,255))	#White
pygame.display.flip()
iterations = 10000
x,y = 1600,1600

for i in range(iterations):
	screen.set_at((int(4*x+800),int(800-4*y)), (0, 255, 0))
	choice = random.randint(1,4)
	if choice == 1:
		x,y = 0.85*x + 0.04*y  ,-0.04*x + 0.85*y + 40  
	elif choice == 2:
		x,y = 0.20*x - 0.26*y  ,  0.23*x + 0.22*y + 40 
	elif choice == 3:
		x,y =-0.15*x + 0.28*y , 0.26*x + 0.24*y + 11
	elif choice == 4:
		x,y =0,  0.16*y  
		screen.set_at((int(4*x+800),int(800-4*y)), (127, 10, 50))
	if i % 1000:
		pygame.display.flip()

str = raw_input("Do you want to save the screen?(y/n)")
if str == "y":
	name = raw_input("Enter name of image : ")
	pygame.image.save(screen, name+".png")
else:
	pygame.quit()
