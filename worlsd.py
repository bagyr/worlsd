import os, sys, math
import pygame
from pygame.locals import *
import pygame.image
from noise import pnoise2

class landscape(object):
    def __init__(self, maxX, maxY):
		(self.width, self.height) = (maxX, maxY)
		self.heightmap = [[0 for i in range(self.width)] \
			for j in range(self.height)]

    def heightFunc(self, radius, x, y, x1, y1):
	if (math.sqrt((x-x1)**2 + (y-y1)**2) > radius):
	    return 0
	else:
	    return (radius-math.sqrt((x-x1)**2 + (y-y1)**2))/radius

    def addMountain(self, height, center = -1, radius = -1):
	if center is -1:
	    center = (int(self.width/2), int(self.height/2))
	if radius is -1:
	    radius = int(self.width/4)
	for x in range(self.width):
	    for y in range(self.height):
		self.heightmap[x][y] += \
			int(height * self.heightFunc \
            (radius, x, y, center[0], center[1]))

    def addNoise(self, octaves):
        freq = 16.0 * octaves
        for x in range(self.width):
            for y in range(self.height):
                self.heightmap[x][y] += \
                        int(pnoise2(x / freq, y / freq, octaves)\
                        * 127.0 + 128.0)

    def drawTexture(self, surf):
        rect = surf.get_rect()
        xsize = rect.width / self.width 
        ysize = rect.height / self.height
        maxValue = max([max(i) for i in self.heightmap])
        minValue = min([min(i) for i in self.heightmap])
        coef = 255.0 / (maxValue - minValue)
        for x in range(self.width):
            for y in range(self.height):
                col = int((self.heightmap[x][y] - minValue) * coef)
                print maxValue
                print minValue
                print col
                print self.heightmap[x][y]
                pygame.draw.rect(surf, (col, col, col),
                        (x*xsize, y*ysize, (x+1)*xsize, (y+1)*ysize))

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    back = pygame.Surface(screen.get_size())
    worlsd = landscape(100, 100)
    worlsd.addMountain(300);
    worlsd.addNoise(2);
    back.fill((0, 0, 0))
    screen.blit(back, (0, 0))
    img = pygame.Surface((600,600))
    worlsd.drawTexture(img);
    screen.blit(img, (0,0))
    pygame.display.flip()
    clock = pygame.time.Clock()
    while 1:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                print 'Done'
                return
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                print 'Done'
                return
            elif event.type == KEYDOWN and event.key == K_LEFT:
                if tresh > 1:
                    tresh -= 1
                    screen.fill((0, 0, 0))
                    drawTex(tex, img, tresh)
                    screen.blit(img, (0, 0))
                    pygame.display.flip()
                    print 'tres', tresh
            elif event.type == KEYDOWN and event.key == K_RIGHT:
                if tresh < 255:
                    tresh += 1
                    screen.fill((0, 0, 0))
                    drawTex(tex, img, tresh)
                    screen.blit(img, (0, 0))
                    pygame.display.flip()
                    print 'tres', tresh
                

if __name__ == '__main__':
    main()
