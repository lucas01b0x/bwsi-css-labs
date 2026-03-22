"""
tests_1d.py

This module contains unit tests for the max_subarray_sum function defined in lab_1d.py.
Some test cases are taken from the Leetcode problem this function pertains to: 
https://leetcode.com/problems/two-sum/ (leetcode easy)
"""

import pytest
from labs.lab_1.lab_1d import two_sum

def tests():
    assert two_sum([2, 7, 11, 15], 9) == [0,1]
    assert two_sum([3,2,4], 6) == [1,2]
    assert two_sum([3,3], 6) == [0,1]

if __name__ == "__main__":
    pytest.main()