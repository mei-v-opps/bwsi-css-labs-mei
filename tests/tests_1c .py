"""
tests_1b.py

This module contains unit tests for the max_subarray_sum function defined in lab_1b.py.
"""

import pytest
from labs.lab_1.lab_1c import max_subarray_sum

def test_addition():
    assert max_subarray_sum([1,2,3,4,5]) == 15          # Test for positive numbers
    assert max_subarray_sum([-1,1,-2,-2,-3]) == 0         # Test for negative and positive number

if __name__ == "__main__":
    pytest.main()