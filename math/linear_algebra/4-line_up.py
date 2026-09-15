#!/usr/bin/env python3
"""Add two arrays element-wise."""


def add_arrays(arr1, arr2):
    """Return a new list containing the element-wise sum."""
    if len(arr1) != len(arr2):
        return None
    return [arr1[i] + arr2[i] for i in range(len(arr1))]
