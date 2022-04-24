import itertools

ts = [(1,1), (1,3), (3,1), (3,3)]
tt = [(2,1), (2,3), (1,1), (1,3)]
oo = [(1.5, 8.0), (4.0, 8.0), (4.0, 1.5), (1.5, 1.5)]

# order corners  DONT NEED ALL OF THIS JUST NEED LL AND UR POINTS
def order_corners(corner_list):
    ordered_corners = []
    tuple_sum = [coord[0]+coord[1] for coord in corner_list]

    # get lower left and upper right corner indices
    lower_left_index = tuple_sum.index(min(tuple_sum))
    upper_right_index = tuple_sum.index(max(tuple_sum))

    # add corners
    ordered_corners.append(corner_list[lower_left_index])
    ordered_corners.append(corner_list[upper_right_index])

    corner_list.remove(ordered_corners[0])
    corner_list.remove(ordered_corners[1])

    # get upper left and lower right indices
    corner_list
    if corner_list[0][0] == ordered_corners[0][0]:
        ordered_corners.insert(1, corner_list[0])
        ordered_corners.insert(2, corner_list[1])
    else:
        ordered_corners.insert(1, corner_list[1])
        ordered_corners.insert(2, corner_list[0])
    
    return ordered_corners

# get LL and UR corners
def get_ll_ur_corners(corner_list):
    tuple_sum = [coord[0]+coord[1] for coord in corner_list]
    ll_index = tuple_sum.index(min(tuple_sum))
    ur_index = tuple_sum.index(max(tuple_sum))
    return [corner_list[ll_index], corner_list[ur_index]]
    

# get ratio 
def calc_spacing(lower_limit, upper_limit, intervals):
    return (upper_limit-lower_limit)/(intervals - 1)


def get_interval_values(lower_limit, upper_limit, interval):
    interval_list = []

    while (lower_limit <= upper_limit):
        interval_list.append(lower_limit)
        lower_limit += interval

    return interval_list
