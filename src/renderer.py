import numpy as np
import examples

FILM_DIMENSIONS = (800, 800)

def bounding_box(polygon):
    """
    Calculates bounding box of a convex polygon.
    
    :param polygon: List of vertices of the polygon.
    :return: The lower left point, the width and the height.
    """
    vtx = polygon.T
    lower_left = np.array([np.min(vtx[0]), np.min(vtx[1])])
    upper_right = np.array([np.max(vtx[0]), np.max(vtx[1])])
    width, height = upper_right - lower_left
    return lower_left, width, height
    
    
def inside_polygon(point, polygon):
    """
    Check if point is inside a convex polygon.
    Uses the ray casting algorithm.
    Points must be in homogeneous coordinates.
    
    :param point: Point to check
    :param polygon: List of vertices of the polygon
    :return: Boolean
    """
    vertex_couples = [(polygon[i-1], polygon[i]) for i in range(len(polygon))]
    
    for vertex in polygon:
        ray = [point, vertex]
        i = 0
        for couple in vertex_couples:
            if between_points(ray, couple):
                i += 1
        if i == 2:
            return False
            
    return True
        

def fill_polygon(polygon, film):
    """
    Fills the film with the points occupied by the polygon.
    
    :param polygon: The polygon
    :param film: The matrix of pixels
    """
    polygon = np.array(polygon)
    (llx, lly), width, height = bounding_box(polygon)
    points = np.array([(x, y, 1)
        for y in range(lly, lly+height+1)
        for x in range(llx, llx+width+1)])
        
    for p in points: 
        if inside_polygon(p, polygon):
            x, y, _ = p
            if 0 < x < 800 and 0 < y < 800:
                film[x][y] = 1


def render(polygons):
    film_w, film_h = FILM_DIMENSIONS
    film = np.array([[0]*film_w]*film_h)
    l = len(polygons)
    i = 0
    polygons = np.array(polygons)
    polygons = (polygons*film_w/2 + film_w/2).astype(int)
    
    for poly in polygons:
        fill_polygon(poly, film)
        
        i += 1
        print i, l
    
    with open('out.ppm', 'w') as f:
        f.write('P5\n800 800\n255\n')
        for row in film:
            for elem in row:
                f.write(chr(elem*255))


def between_points(ray, points):
    """
    Check if the ray defined by two points of it
    passes through the two given points.
    Points must be in homogeneous coordinates.
    
    :param ray: Two points that defines the ray.
    :param points: Two points.
    :return: Boolean
    """
    v1 = (points[0][0]-ray[0][0])*(ray[0][1]-ray[1][1]) - \
        (points[0][1]-ray[0][1])*(ray[0][0]-ray[1][0])
    v2 = (points[1][0]-ray[0][0])*(ray[0][1]-ray[1][1]) - \
        (points[1][1]-ray[0][1])*(ray[0][0]-ray[1][0])
    return v1*v2 <= 0


if __name__=='__main__':
    poly = np.array([
        [400, 400,   1],
        [480, 400,   1],
        [480, 440,   1],
        [400, 480,   1]])

    point = [440, 440, 1]
    
    
    branches = examples.side_tree()
    
    polys = []
    for branch in branches:
        polys += branch
        
    render(polys)
    
    
    
    
