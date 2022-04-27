import pixel_util as p_util

class ImgController:

    def __init__(self, ImgModel=None) -> None:
        self.model = ImgModel

    def parse_size(self, string_size_list):
        """Takes list of paramaters as strings and sets size for image"""

        size = (float(string_size_list[0]), float(string_size_list[1]))
        self.model.set_size(size)

    def parse_corners(self, corners_string):
        """Takes list of parameters as strings and sets corners for image"""

        corners = [float(i) for i in corners_string]
        corners_list = [(corners[0], corners[1]), (corners[2], corners[3]), (corners[4], corners[5]), (corners[6], corners[7])]
        self.model.set_corners(corners_list)

    def get_ll_ur_corners(self):
        """Gets the lower left and upper right corners from models corner list"""
        return p_util.get_ll_ur_corners(self.model.get_corners())
    
    def get_xy_coordinates(self):
        """Uses models lower left and upper right corners to generate images x and y coordinates"""

        # get size and corners
        size = self.model.get_size()
        corners = self.get_ll_ur_corners()

        # set all x and y coordinates based on distance and img size
        x_coords = p_util.get_coordinates(corners[0][0], corners[1][0], size[0])
        y_coords = p_util.get_coordinates(corners[0][1], corners[1][1], size[1])

        return [x_coords, y_coords]

    def solve(self):
        """Extracts model data and creates grid solution"""
        
        # cartesian product of images x and y coordinate lists
        xy_coordinates = self.get_xy_coordinates()
        solution = p_util.cartesian_prod(xy_coordinates[0], xy_coordinates[1])

        # sets models solution
        self.model.set_solution(solution)

        return solution

    def get_solution(self):
        """Returns solution of model"""
        return self.model.get_solution()
    
    def clear_solution(self):
        """removes model's solution"""
        self.model.set_solution([])
    