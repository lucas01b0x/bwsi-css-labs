"""
tests_1c.py

This module contains unit tests for the max_subarray_sum function defined in lab_1c.py.
Some test cases are taken from the Leetcode problem this function pertains to: 
https://leetcode.com/problems/maximum-subarray/ (leetcode medium)
"""

import pytest
from labs.lab_1.lab_1c import max_subarray_sum

def tests():
    assert max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]) == 6
    assert max_subarray_sum([5,4,-1,7,8]) == 23
    assert max_subarray_sum([1]) == 1

if __name__ == "__main__":
    pytest.main()