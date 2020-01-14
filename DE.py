# !/usr/bin/env python
# --------------------------------------------------------------
# File:          DE.py
# Project:       PyEvoAlg
# Created:       Sunday, 8th December 2019 12:24:18 pm
# @Author:       Molin Liu, MSc in Data Science
# Contact:       molin@live.cn
# Last Modified: Sunday, 8th December 2019 12:24:22 pm
# Copyright  © Rockface 2019 - 2020
# --------------------------------------------------------------

import individual


class DE:
    '''
    Implementation of Differential Evolution
    C_M: constraint matrix
    '''

    def __init__(self, F, N, G, constraint_matrix):
        '''
        Variables assignment
        '''
        self.F = F
        self.G = G
        self.N = N

        '''
        Initialization
        '''
        self.P = []

    def _init_P(self):
        raise NotImplementedError
