#!/usr/bin/env python3
'''
    A function that performs matrix multiplication:
'''


def mat_mul(mat1, mat2):
    '''
        performing matrix multiplication:
    '''
    if len(mat1[0]) == len(mat2):
        return mat1 @ mat2
    else:
        return None
