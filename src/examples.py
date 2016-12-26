import numpy as np

import utilities as util
import branches as br

def top_tree():
    br_angle_fn = util.random_between(
        [ -np.pi/12, +np.pi/12, -np.pi/12 ], 
        [  -np.pi/4,  +np.pi/4, +np.pi/12 ])
    
    branch_fn = br.branch(
        angle_fn = br_angle_fn,
        height_fn = util.random_between(.05, .15),
        delta_width = -.009)
    
    angle_fn = util.random_between(-np.pi/16, np.pi/16)

    return [branch_fn(.05, util.r_mat(angle + angle_fn()))
        for angle in util.sample_interval(0, 2*np.pi, 5)]


def side_tree():
    br_angle_fn = util.random_between(
        [ -np.pi/12, +np.pi/12 ], 
        [  -np.pi/6,  +np.pi/6 ])
    
    branch_fn = br.branch(
        angle_fn = br_angle_fn,
        height_fn = util.random_between(.05, .15),
        delta_width = -.009)
    
    angle_fn = util.random_between(-np.pi/16, np.pi/16)

    return [branch_fn(.1, util.t_mat([0, -.5]))]

def snowflake():
    
    angle = np.pi/4
    angle_fn = lambda: [0, -angle, angle]
    
    params = [
        dict(   
            angle_fn = angle_fn,
            height_fn = lambda: .15,
            delta_width = -.014
        ),
        dict(   
            angle_fn = angle_fn,
            height_fn = lambda: .15,
            delta_width = -.014
        )]
    
    
    branch_fns = [br.branch(**param)
            for param in params]
    
    angles = util.sample_interval(0, 2*np.pi, 4)
    
    return \
        [branch_fns[0](.05, util.t_mat([0,-.5])) for a in angles] + \
        [branch_fns[1](.04, util.t_mat([0,-.5])) for a in angles]

