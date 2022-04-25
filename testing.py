import unittest
import pixel_coordinator as pix_coord


class TestClassCorners(unittest.TestCase):
    """Test getting lower left and upper right corners from unordered list of tuples"""

    def test_positive(self):
        test_list = [(1, 1), (3, 3), (3, 1), (1, 3)]
        corners = [(1,1), (3,3)]

        self.assertEqual(pix_coord.get_ll_ur_corners(test_list), corners, "Positive Case Failed")
    
    def test_doubles(self):
        test_list = [(4.0, 1.5), (4.0, 8.0), (1.5, 1.5), (1.5, 8.0)]
        corners = [(1.5, 1.5), (4.0, 8.0)]

        self.assertEqual(pix_coord.get_ll_ur_corners(test_list), corners, "Double Case Failed")

    def test_negatives(self):
        test_list = [(-1, -1), (-5, -5), (-1, -5), (-5, -1)]
        corners = [(-5, -5), (-1, -1)]

        self.assertEqual(pix_coord.get_ll_ur_corners(test_list), corners, "Negative Case Failed")

    def test_mixed(self):
        test_list = [(-2, -2), (-2, 2), (2, 2), (2, -2)]
        corners = [(-2, -2), (2, 2)]

        self.assertEqual(pix_coord.get_ll_ur_corners(test_list), corners, "Mixed Case Failed")


class TestClassIntervalSpacing(unittest.TestCase):
    """Test interval space funciton"""
    
    def test_positive(self):
        self.assertEqual(pix_coord.calc_spacing(1, 3, 3), 1, "Positive Case Failed")

    def test_negative(self):
        self.assertEqual(pix_coord.calc_spacing(-2, -1, 3), 0.5, "Negative Case Failed")


class TestClassCoordinates(unittest.TestCase):
    """Test coordinate generating function"""

    def test_positive(self):
        coord_list = [1.0, 1.5, 2.0]

        self.assertEqual(list(pix_coord.get_coordinates(1, 2, 3)), coord_list, "Positive Case Failed")

    def test_negative(self):
        coord_list = [-2.0, -1.5, -1.0]

        self.assertEqual(list(pix_coord.get_coordinates(-2, -1, 3)), coord_list, "Negative Case Failed")


class TestClassCartesianRow(unittest.TestCase):
    "Testing cartesian product helper funciton"

    def test_positive(self):
        outcome = [[1, 1], [2, 1], [3, 1]]

        self.assertEqual(pix_coord.cartesian_row([1, 2, 3], 1), outcome, "Positive Case Failed")
    
    def test_negative(self):
        outcome = [[-2.0, 1], [-1.5, 1], [-1.0, 1]]

        self.assertEqual(pix_coord.cartesian_row([-2.0, -1.5, -1.0], 1), outcome, "Positive Case Failed")


def run_tests():
    """Run specified tests"""

    tests_to_run = [TestClassCorners, TestClassIntervalSpacing, TestClassCoordinates, TestClassCartesianRow]

    loader = unittest.TestLoader()

    suite_list = []

    for test in tests_to_run:
        suite = loader.loadTestsFromTestCase(test)
        suite_list.append(suite)
    
    full_suite = unittest.TestSuite(suite_list)

    runner = unittest.TextTestResult()
    results = runner.run(full_suite)


if __name__ == '__main__':
    unittest.main()
    #run_tests()

