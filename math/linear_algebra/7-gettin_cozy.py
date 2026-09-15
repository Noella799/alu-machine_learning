#!/usr/bin/env python3
"""Concatenate two 2D matrices along a given axis."""


def cat_matrices2D(mat1, mat2, axis=0):
    """Return a new matrix concatenating mat1 and mat2 along axis."""
    if axis == 0:
        if len(mat1[0]) != len(mat2[0]):
            return None
        return [row[:] for row in mat1] + [row[:] for row in mat2]
    if axis == 1:
        if len(mat1) != len(mat2):
            return None
        if any(len(row) != len(mat2[0]) for row in mat2):
            return None
        return [mat1[i][:] + mat2[i][:] for i in range(len(mat1))]
    return None
