import numpy as np

# get LL and UR corners
def get_ll_ur_corners(corner_list: tuple) -> list:
    """Get lower left and upper right corners from corner lists"""

    tuple_sum = [coord[0]+coord[1] for coord in corner_list]
    ll_index = tuple_sum.index(min(tuple_sum))
    ur_index = tuple_sum.index(max(tuple_sum))
    return [corner_list[ll_index], corner_list[ur_index]]
    
# get distance between coordinates 
def calc_spacing(lower_limit, upper_limit, intervals) -> float:
    """Calculate the distance between each pixel"""

    return abs((upper_limit-lower_limit)/(intervals - 1))

# get list of coordinates
def get_coordinates(lower_limit, upper_limit, intervals):
    """Get equally spaced values between lower and upper limit for pixels"""

    return np.linspace(lower_limit, upper_limit, int(intervals), endpoint=True)

# helper function to create rows in cartesian_prod
def cartesian_row(x_array, y):
    """Cartesian product of n-dimension array and single y-coordinate"""

    row = []
    for x in x_array:
        row.append([round(x, 2), round(y, 2)])
    return row

# cartesian product of two arrays
def cartesian_prod(x_array, y_array):
    """Cartesian product of two arrays in requested format"""

    prod = []
    for y in reversed(y_array):
        prod.append(cartesian_row(x_array, y))
    return prod
