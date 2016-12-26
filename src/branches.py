import numpy as np
import utilities as util

import glutilities as glutil

def segment(matrix, lower_width, upper_width, height):
    """
    Generates a isosceles trapezoid of given dimensions and transform it
    accordingly to the given transformation matrix.
    The origin of the trapezoid is on the lower base middle point.
    
    :param matrix: Transformation matrix
    :param lower_width: Length of the lower base of the trapezoid
    :param upper_width: Length of the upper base of the trapezoid
    :param height: Height of the trapezoid
    :return: Tuple with: the given matrix centered to the upper base middle 
        point of the trapezoid cone and a list of 5 vertices in world coords
    """
    local_points = np.array([
        [               0, height, 1 ],
        [ -upper_width/2., height, 1 ],
        [ -lower_width/2.,      0, 1 ],
        [ +lower_width/2.,      0, 1 ],
        [ +upper_width/2., height, 1 ]])
    
    world_points = np.dot(local_points, matrix)    
    matrix[2] = world_points[0]
    
    return matrix, world_points[1:]
    
    
def branch(angle_fn, height_fn, delta_width):
    """
    Generates a function for generating branches.
    
    :param angle_fn: Function that returns a tuple of floats.
        The dimension of the returned value determines how many branches
        are generated for every recursive step of the generated function.
    :param height_fn: Function that returns an height of a segment
    :param delta_width: Delta of the segment width at every recursion.
        Must be negative.
    :return: Function to generate branches.
    """
    def loop(start_width, start_matrix):
        """
        Generates recursively a branch made with trapezoids.
        It will loops until the start_width is greater than the
        absolute of delta_width (which is defined in branch()).
        
        :param start_width: Start length of the lower base of the next trapezoid
        :param start_matrix: Transformation matrix
        """
        if start_width <= abs(delta_width):
            return []
        else:
            upper_width = start_width + delta_width
            new_mat, points = segment(
                start_matrix,
                start_width,
                upper_width,
                height_fn())
            
            angles = angle_fn()
            mats = [np.dot(util.r_mat(alpha), new_mat) for alpha in angles]
            
            glutil.draw_poly(points, fill=True)
            
            pts = [points]
            for mat in mats:
                pts += loop(upper_width, mat)
                
            return pts
            
    return loop

