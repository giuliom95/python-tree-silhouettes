import numpy as np

def random_between(lower_bound, upper_bound):
    """
    Generates a function that returns a value between the given ones.
    
    :param lower_bound: A number or an iterable made of numbers that indicates
        the lower bound of the values returned by the generated func.
    :param upper_bound: A number or an iterable made of numbers that indicates
        the upper bound of the values returned by the generated func.
    :return: Function that returns a numpy array in the given range.
        The array dimensions are the same of lower_bound and upper_bound
    """
    lb = np.array(lower_bound)
    ub = np.array(upper_bound)
    delta = ub - lb
    def fn(multiplier=1, *args):
        return np.multiply(multiplier*delta, np.random.random()) + lb
    return fn


def sample_interval(lower_bound, upper_bound, samples):
    """
    Subdivides the interval between the given bounds in many equal samples.
    
    :param lower_bound: A number or an iterable made of numbers that indicates
        the lower bound of the interval to sample
    :param upper_bound: A number or an iterable made of numbers that indicates
        the upper bound of the interval to sample
    :param samples: Number of samples to return
    :return: A list of samples of the same dimension of the given bounds
    """
    lb = np.array(lower_bound)
    ub = np.array(upper_bound)
    delta = (1./samples)*(ub - lb)
    return [lb+i*delta for i in range(samples)]
    

def r_mat(angle):
    """
    Builds the rotation matrix of the given angle
    :param angle: Angle expressed in radians
    :return: 3x3 numpy array
    """
    sin = np.sin(angle)
    cos = np.cos(angle)
    return np.array([
        [ +cos, +sin, 0 ],
        [ -sin, +cos, 0 ],
        [    0,    0, 1 ]], dtype=float)
        

def t_mat(vec):
    """
    Builds the translation matrix of the given vector
    :param vec: Translation vector
    :return: 3x3 numpy array
    """
    return np.array([
        [      1,      0, 0 ],
        [      0,      1, 0 ],
        [ vec[0], vec[1], 1 ]], dtype=float)

