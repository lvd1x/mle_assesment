import model
import pixel_util as p_util

class ImgController:

    def __init__(self, ImgModel) -> None:
        self.model = ImgModel

    def parse_size(self, size_token):
        return 

    def parse_corners(self, corners_token):
        return 

    def get_ll_ur_corners(self):
        """Gets the lower left and upper right corners from models corner list"""
        return p_util.get_ll_ur_corners(self.model.get_corners())
    
    def get_xy_coordinates(self):
        """Uses models lower left and upper right corners to generate images x and y coordinates"""

        # gets 
        size = self.model.get_size()
        corners = self.get_ll_ur_corners()

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
    

        