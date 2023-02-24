#!/bin/python3
'''
Python provides built-in sort/sorted functions that use timsort internally.
You cannot use these built-in functions anywhere in this file.

Every function in this file takes a comparator `cmp` as input
If cmp(a, b) returns -1, then a < b;
if cmp(a, b) returns  1, then a > b;
if cmp(a, b) returns  0, then a == b.
'''


def cmp_standard(a, b):
    '''
    used for sorting from lowest to highest


    >>> cmp_standard(125, 322)
    -1
    >>> cmp_standard(523, 322)
    1
    '''
    if a < b:
        return -1
    if b < a:
        return 1
    return 0


def cmp_reverse(a, b):
    '''
    used for sorting from highest to lowest

    >>> cmp_reverse(125, 322)
    1
    >>> cmp_reverse(523, 322)
    -1
    '''
    if a < b:
        return 1
    if b < a:
        return -1
    return 0


def cmp_last_digit(a, b):
    '''
    used for sorting based on the last digit only

    >>> cmp_last_digit(125, 322)
    1
    >>> cmp_last_digit(523, 322)
    1
    '''
    return cmp_standard(a % 10, b % 10)


def _merged(xs, ys, cmp=cmp_standard):
    '''

    >>> _merged([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    '''
    ixs = 0
    iys = 0
    ret = []
    while ixs < len(xs) and iys < len(ys):
        if cmp(xs[ixs], ys[iys]) == -1:
            ret.append(xs[ixs])
            ixs += 1
        else:
            ret.append(ys[iys])
            iys += 1

    while ixs < len(xs):
        ret.append(xs[ixs])
        ixs += 1

    while iys < len(ys):
        ret.append(ys[iys])
        iys += 1

    return ret


def merge_sorted(xs, cmp=cmp_standard):
    '''
    Merge sort is the standard O(n log n) sorting algorithm.
    Recall that the merge sort pseudo code is:

        if xs has 1 element
            it is sorted, so return xs
        else
            divide the list into two halves left,right
            sort the left
            sort the right
            merge the two sorted halves

    You should return a sorted version of the input list xs.
    You should not modify the input list xs in any way.
    '''
    if len(xs) <= 1:
        return xs
    else:
        mid = len(xs) // 2
        left = xs[mid:]
        right = xs[:mid]
        left_sorted = merge_sorted(left, cmp=cmp)
        right_sorted = merge_sorted(right, cmp=cmp)
        return _merged(left_sorted, right_sorted, cmp=cmp)


def quick_sorted(xs, cmp=cmp_standard):
    '''
    You should return a sorted version of the input list xs.
    You should not modify the input list xs in any way.
    '''
    if len(xs) <= 1:
        return xs
    else:
        mid = len(xs) // 2
        pivot = xs[mid]
        xs_lt = [x for x in xs if cmp(x, pivot) == -1]
        xs_gt = [x for x in xs if cmp(x, pivot) == 1]
        xs_eq = [x for x in xs if cmp(x, pivot) == 0]
        xs_lt = quick_sorted(xs_lt, cmp=cmp)
        xs_gt = quick_sorted(xs_gt, cmp=cmp)
        return xs_lt + xs_eq + xs_gt


def quick_sort(xs, cmp=cmp_standard):
    '''
    EXTRA CREDIT:
    The main advantage of quick_sort is that it can be implemented "in-place".
    This means that no extra lists are allocated,
    or that the algorithm uses Theta(1) additional memory.
    Merge sort, on the other hand, must allocate intermediate
    lists for the merge step,
    and has a Theta(n) memory requirement.
    Even though quick sort and merge sort both have the same
    Theta(n log n) runtime,
    this more efficient memory usage typically makes quick
    sort faster in practice.
    (We say quick sort has a lower "constant factor" in its runtime.)
    The downside of implementing quick sort in this way is that it
    will no longer be a [stable sort]
    (https://en.wikipedia.org/wiki/Sorting_algorithm#Stability),
    but this is typically inconsequential.

    Follow the pseudocode of the Lomuto partition
    scheme given on wikipedia
    (https://en.wikipedia.org/wiki/Quicksort#Algorithm)
    to implement quick_sort as an in-place algorithm.
    You should directly modify the input xs variable
    instead of returning a copy of the list.
    '''
    lo = 0
    hi = len(xs) - 1

    def partition(xs, lo, hi):
        pivot = xs[hi]
        i = lo - 1
        for j in range(lo, hi - 1):
            if xs[j] <= pivot:
                i += 1
                (xs[i], xs[j]) = (xs[j], xs[i])
        (xs[i + 1], xs[hi]) = (xs[hi], xs[i + 1])
        return i + 1
    if lo < hi:
        part = partition(xs, lo, hi)
        quick_sort(xs, lo, part - 1)
        quick_sort(xs, part + 1, hi)

    return xs
