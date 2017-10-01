# -*- coding: utf-8 -*-
#!/usr/bin/python

from __future__ import print_function
import random
import time
import sorting


"""
Test basic sorting algorithms implemented in Python
By jeven 2017
"""

def generate_random(n, range_left, range_right):
    """
    Test helpler for generating test arrays
    """
    assert range_right >= range_left
    arr = []
    for i in xrange(n):
        arr.append(random.randrange(range_left, range_right))
    return arr


def test_sort(sort_algo, arr, n):
    """
    sort_algo: sorting algorithm
    arr: list of numbers to be sorted
    n: length of the list
    """
    assert arr != None
    try:
        start_time = time.clock()
        arr_after_sort = sort_algo(arr, n)
        end_time = time.clock()
        # print("List after sort:", arr_after_sort)
        print("Is sorted:", is_sorted(arr_after_sort))
        assert arr_after_sort == sorted(arr)
        print("Time consumed(s):", end_time-start_time)
    except AssertionError as a:
        print('Sorting failed...')
    except Exception as e:
        raise e


def is_sorted(arr):
    return all(arr[i] <= arr[i+1] for i in xrange(len(arr)-1))


if __name__ == '__main__':
    n = 1000
    arr = generate_random(n, 0, 10000)
    test_sort(sorting.quick_sort, arr, n)
