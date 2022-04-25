import itertools
import numpy as np

ts = [(1,1), (1,3), (3,1), (3,3)]
tt = [(2,1), (2,3), (1,1), (1,3)]
oo = [(1.5, 8.0), (4.0, 8.0), (4.0, 1.5), (1.5, 1.5)]

# get LL and UR corners
def get_ll_ur_corners(corner_list):
    tuple_sum = [coord[0]+coord[1] for coord in corner_list]
    ll_index = tuple_sum.index(min(tuple_sum))
    ur_index = tuple_sum.index(max(tuple_sum))
    return [corner_list[ll_index], corner_list[ur_index]]
    

# get distance between coordinates 
def calc_spacing(lower_limit, upper_limit, intervals):
    return (upper_limit-lower_limit)/(intervals - 1)

# get list of coordinates
def get_coordinates(lower_limit, upper_limit, intervals):
    return np.linspace(lower_limit, upper_limit, intervals, endpoint=True)


# helper function to create rows
def cartesian_row(x_array, y):
    row = []
    for x in x_array:
        row.append([x, y])
    return row

# cartesian product of two arrays
def cartesian_prod(x_array, y_array):
    prod = []
    for y in reversed(y_array):
        prod.append(cartesian_row(x_array, y))
    return prod

