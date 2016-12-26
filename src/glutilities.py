from OpenGL.GL import *
import pygame

def draw_poly(points, delay=0, fill=True):    
    
    draw_type = GL_POLYGON if fill else GL_LINE_LOOP

    glBegin(draw_type)
    for point in points:
        glVertex(point)
    glEnd()
    pygame.display.flip()
    
    glBegin(draw_type)
    for point in points:
        glVertex(point)
        
    glEnd()
    pygame.display.flip()    
    
    pygame.time.delay(delay)
    
        
def draw_ref(matrix, axes_length=.1):
    """
    Draws (via OpenGL) the ref axes of the given reference system
    
    :param matrix: Transformation matrix of the refernce
    :param axes_length: Non-deformed length of the axes.
    """
    
    points = np.array([
        [           0,           0, 1 ],
        [ axes_length,           0, 1 ],
        [           0, axes_length, 1 ]])
        
    w_points = np.dot(points, matrix)
    
    glBegin(GL_LINES)
    glColor(1, 0, 0)
    glVertex(w_points[0])
    glVertex(w_points[1])
    glColor(0, 1, 0)
    glVertex(w_points[0])
    glVertex(w_points[2])
    glEnd()
    glColor(1, 1, 1)
