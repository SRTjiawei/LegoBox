# -*- coding: utf-8 -*-
#!/usr/bin/python

from __future__ import print_function
import random

"""
Basic sorting algorithms implemented in Python
By jeven 2017
"""


def insertion_sort(arr, n):
    """
    Insertion sort, optimized
    comlexity: worst - O(n^2)
    """
    for i in xrange(n):
        tmp = arr[i]
        for j in xrange(i, 0, -1):
            if tmp < arr[j-1]:
                arr[j] = arr[j-1]
            else:
                arr[j] = tmp
    return arr

def selection_sort(arr, n):
    """
    Selection sort,
    comlexity: worst - O(n^2)
    """
    for i in xrange(n):
        for j in xrange(i+1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


def shell_sort(arr, n):
    # TODO:
    pass


def bubble_sort(arr, n):
    """
    Bubble_sort, enhanced
    comlexity: worst - O(n^2)
    """
    for i in xrange(n):
        max_idx = n-i-1
        for j in xrange(0, n-i-1):
            if arr[j] > arr[max_idx]:
                max_idx = j
        arr[n-i-1], arr[max_idx] = arr[max_idx], arr[n-i-1]
    return arr


def merge_sort(arr, n):
    """
    merge sort,
    complexity: O(nlog(n))
    """
    _merge_sort(arr, 0, n-1)
    return arr


def _merge_sort(l, left, right):
    """
    Recursive helpler function only for merge_sort
    """
    if left >= right:
        return
    mid = (left + right) / 2
    _merge_sort(l, left, mid)
    _merge_sort(l, mid+1, right)
    _merge(l, left, mid, right)


def _merge(l, left, mid, right):
    """
    Helpler function only for _merge_sort
    Complexity O(n)
    """
    # make a copy of lists to merge
    tmp = l[left:right+1]
    # each sublist has an indicator
    i = left
    j = mid + 1
    # merge two sublists into one
    for k in xrange(left, right+1):
        if i > mid:
            l[k] = tmp[j-left]
            j += 1
        elif j > right:
            l[k] = tmp[i-left]
            i += 1
        elif tmp[i-left] < tmp[j-left]:
            l[k] = tmp[i-left]
            i += 1
        elif tmp[i-left] >= tmp[j-left]:
            l[k] = tmp[j-left]
            j += 1


def _quick_sort(arr, start, end):
    """
    Recursive helpler function
    """
    if start < end:
        pos = _partition(arr, start, end)
        _quick_sort(arr, start, pos-1)
        _quick_sort(arr, pos+1, end)

def _partition(arr, start, end):
    """
    Partition helpler function
    """
    # select the first element as pivot
    pivot = arr[start]
    # select a random ele as pivot
    # pivot = arr[start]
    i = start
    for j in xrange(start+1, end+1):
        if arr[j] < pivot:
            arr[i+1], arr[j] = arr[j], arr[i+1]
            # move the boundary forward
            i += 1
    # move the pivot to the boundary
    arr[i], arr[start] = arr[start], arr[i]
    return i

def quick_sort(arr, n):
    """
    Quick sort,
    Complexity: average O(nlog(n))
    """
    _quick_sort(arr, 0, n-1)
    return arr
