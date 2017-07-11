import pygame
import math
width = 1600
height = 1600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Sierpinki Triangle')
clock = pygame.time.Clock()
screen.fill((125,0,0))

def gen_midpoint(p1, p2):
	p = ((p1[0] + p2[0]) / 2.0, (p1[1] + p2[1]) / 2.0)
	return p

def s_triangle((p1,p2,p3),flip,count):
	colour = ((count/10.0)*flip*255,(count/10.0)*flip*255,(count/10.0)*flip*255) 
	pygame.draw.polygon(screen, colour,(p1,p2,p3),0)
	if flip:
		flip = 1
	else: 
		flip = 1 
	pygame.display.flip()
	clock.tick(20)
	if not count > 5:
		s_triangle((p1, gen_midpoint(p1, p2), gen_midpoint(p1, p3)),flip,count+1)
		s_triangle((p2, gen_midpoint(p2, p3), gen_midpoint(p1, p2)),flip,count+1)
		s_triangle((p3, gen_midpoint(p3, p2), gen_midpoint(p1, p3)),flip,count+1)
pointlist = ((0+800-400,1600-800-100),(800+800-400,1600-800-100),(400+800-400,908-800-100))
s_triangle(pointlist,0,0)
pygame.display.flip()
while(1):
	pass
