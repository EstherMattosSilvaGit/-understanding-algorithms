import unittest
from BinarySearch.binary_search import BinarySearch

class TestBinarySearch(unittest.TestCase):
    def setUp(self):
        self.solution = BinarySearch()

    def test_target_found_middle(self):
        nums = [-1, 0, 3, 5, 9, 12]
        self.assertEqual(self.solution.search(nums, 9), 4)

    def test_target_found_start(self):
        nums = [-1, 0, 3, 5, 9, 12]
        self.assertEqual(self.solution.search(nums, -1), 0)

    def test_target_found_end(self):
        nums = [-1, 0, 3, 5, 9, 12]
        self.assertEqual(self.solution.search(nums, 12), 5)

    def test_target_not_found(self):
        nums = [-1, 0, 3, 5, 9, 12]
        self.assertEqual(self.solution.search(nums, 2), -1)

    def test_empty_list(self):
        nums = []
        self.assertEqual(self.solution.search(nums, 1), -1)

    def test_single_element_found(self):
        nums = [5]
        self.assertEqual(self.solution.search(nums, 5), 0)

    def test_single_element_not_found(self):
        nums = [5]
        self.assertEqual(self.solution.search(nums, 3), -1)

    def test_two_elements_found_first(self):
        nums = [1, 2]
        self.assertEqual(self.solution.search(nums, 1), 0)

    def test_two_elements_found_second(self):
        nums = [1, 2]
        self.assertEqual(self.solution.search(nums, 2), 1)

    def test_two_elements_not_found(self):
        nums = [1, 2]
        self.assertEqual(self.solution.search(nums, 3), -1)

if __name__ == '__main__':
    unittest.main()
