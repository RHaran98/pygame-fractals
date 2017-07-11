import pygame
import math
import cmath
from numpy import complex
width = 1600
height = 1600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Mandelbrot set')
clock = pygame.time.Clock()
screen.fill((125,0,0))
green = 255
blue = 255
max_iter = 20

#s_triangle(pointlist,0,0)
count = 0
for row in range(0,height):
	for col in range(0,width):
		c_re = (col - width/2.0)*4.0/width
		c_im = (row - height/2.0)*4.0/width
		x = y = 0
		i = 0
		while (x*x+y*y <= 4 and i < max_iter):
			x_new = x*x - y*y + c_re
			y = 2*x*y + c_im
			x = x_new
			i = i+1
			print i
			count = count + 1
		if (i < max_iter):
			#screen.set_at((int(col),int(row)), (255,255,255))
			screen.set_at((int(col),int(row)), (255-i, 0, 0))
		else:
			screen.set_at((int(col),int(row)), (0, 0, 0))
		if count%100000 == 0: 
			pygame.display.flip()
pygame.display.flip()
str = raw_input("Do you want to save the screen?(y/n)")
if str == "y":
	name = raw_input("Enter name of image : ")
	pygame.image.save(screen, name+".png")
else:
	pygame.quit()
