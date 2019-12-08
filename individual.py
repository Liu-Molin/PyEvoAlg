# !/usr/bin/env python
# --------------------------------------------------------------
# File:          individual.py
# Project:       PyEvoAlg
# Created:       Sunday, 8th December 2019 1:43:00 pm
# @Author:       Molin Liu, MSc in Data Science
# Contact:       molin@live.cn
# Last Modified: Sunday, 8th December 2019 1:43:02 pm
# Copyright  © Rockface 2019 - 2020
# --------------------------------------------------------------
import numpy as np


class Individual:
    '''
    Store the parameters and the corresponding objective values.
    '''

    def __init__(self, param, objective_fn: list):
        self.param = param
        self.ov = np.array([of(param) for of in objective_fn])

    def __str__(self):
        return 'Param:\t' + str(self.param) + '\nObjective:\t' + str(self.ov)
