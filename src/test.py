import pygame
from pygame.locals import *
from OpenGL.GL import *

import examples

SCREEN_SIZE = (800, 800)
   

def main():
    
    pygame.init()
    pygame.display.set_mode(SCREEN_SIZE, DOUBLEBUF | OPENGL)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    
    branches = examples.side_tree()    
    
    for branch in branches:
        for segment in branch:
            glBegin(GL_POLYGON)
            for point in segment:
                glVertex(point)
            glEnd()
    
            
    pygame.display.flip()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() 
                return
            
        pygame.time.delay(100)


if __name__ == '__main__':
    main()
