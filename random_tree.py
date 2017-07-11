import pygame
import random
import math
width = 1600
height = 1600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Fractal')
clock = pygame.time.Clock()
screen.fill((0,0,0))

def fractal2(screen,x,y,len,angle,count):
	x2 = x + len*(math.sin(angle))
	y2 = y + len*(math.cos(angle))
	if not ((x > width or x < 0) or (y > height or y < 0) or count > 6):
		num = random.randint(4,9)
		for i in range(1,num):
			angle_diff = (random.random()-0.5)*(math.pi/2)
			factor = random.random()
			fractal2(screen,x2,y2,(len*(factor)),(angle+(angle_diff)),count+1)
	
	else:
		return
	pygame.draw.line(screen,(127,0,0),(x,y),(x2,y2))
	big_dot(screen,(int(x),int(y)),(0,0,0))	
			
def big_dot(screen,(x,y), (red, green, blue)):
	screen.set_at((x-1,y-1), (red, green, blue))
	screen.set_at((x-1,y), (red, green, blue))
	screen.set_at((x-1,y+1), (red, green, blue))
	screen.set_at((x,y-1), (red, green, blue))
	screen.set_at((x,y), (red, green, blue))
	screen.set_at((x,y+1), (red, green, blue))
	screen.set_at((x+1,y-1), (red, green, blue))
	screen.set_at((x+1,y), (red, green, blue))
	screen.set_at((x+1,y+1), (red, green, blue))
	#pygame.draw.circle(screen,(127, 127, 127),(x,y),1,0) #Uncomment to get vertices

fractal2(screen,width/2,height/2,200,math.pi,0)
pygame.display.flip()

str = raw_input("Do you want to save the screen?(y/n)")
if str == "y":
	name = raw_input("Enter name of image : ")
	pygame.image.save(screen, name+".png")
else:
	pygame.quit()		
		
