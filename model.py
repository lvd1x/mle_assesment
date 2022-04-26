class ImgModel:

    def __init__(self, size=[], corners=[]):
        self.size = size
        self.corners = corners
        self.solution = []
    
    def has_solution(self) -> bool:
        """Returns true if image grid has been produced"""
        return len(self.solution) > 0

    def set_solution(self, solution):
        """sets image grid"""

        self.solution = solution

    def get_solution(self):
        """Returns current image solution"""
        return self.solution

    def set_size(self, size):
        """Sets image size"""

        self.size = size

    def get_size(self):
        """Returns image size"""

        return self.size

    def set_corners(self, corners):
        """Sets image corners"""

        self.corners = corners

    def get_corners(self):
        """Returns image corners"""

        return self.corners