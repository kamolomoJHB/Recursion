import unittest
import super_algos
from unittest.mock import patch
from io import StringIO

class TestAlgos(unittest.TestCase):
    @patch("sys.stdin",StringIO("[5,1,5,7,6]\n[]"))
    def test_find_min_correct(self):
        self.assertEqual(super_algos.find_min([5,1,5,7,6]),min([5,1,5,7,6]))

    def test_list_empty(self):
        self.assertEqual(super_algos.find_min([]),-1)
        self.assertEqual(super_algos.sum_all([]), -1)

    def test_accepted_input_only(self):
        self.assertEqual(super_algos.find_min([5,1,5,7,'x']),-1)
        self.assertEqual(super_algos.sum_all([5,1,5,7,'x']),-1)

    def test_sum_all_correct(self):
        self.assertEqual(super_algos.sum_all([5,5,6,4,2,8]),sum([5,5,6,4,2,8]))

    def test_count_possible_strings_correct(self):
        self.assertEqual(len(super_algos.find_possible_strings(['x','y'], 3)), 8)
    
    def test_no_repetition_in_possible_strings(self):
        list_count_strings = super_algos.find_possible_strings(['x','y'], 3)
        set_count_strings = set(list_count_strings)
        self.assertEqual(len(list_count_strings), len(set_count_strings))
    
    def test_set_input_to_compute_possible_strings(self):
        self.assertEqual(super_algos.find_possible_strings(['x','x'], 3), -1)
