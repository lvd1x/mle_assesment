class ImgModel:

    def __init__(self, size=[], corners=[]):
        self.size = size
        self.corners = corners
        self.solution = []
    
    def has_solution(self) -> bool:
        return len(self.solution) > 0

    def set_solution(self, solution):
        self.solution = solution

    def get_solution(self):
        return self.solution

    def set_size(self, size):
        self.size = size

    def get_size(self):
        return self.size

    def set_corners(self, corners):
        self.corners = corners

    def get_corners(self):
        return self.corners