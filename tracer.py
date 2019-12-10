# !/usr/bin/env python
# --------------------------------------------------------------
# File:          tracer.py
# Project:       PyEvoAlg
# Created:       Sunday, 8th December 2019 12:25:31 pm
# @Author:       Molin Liu, MSc in Data Science
# Contact:       molin@live.cn
# Last Modified: Sunday, 8th December 2019 12:25:32 pm
# Copyright  © Rockface 2019 - 2020
# --------------------------------------------------------------
from individual import Individual
from GA_support import dominate


class Tracer:
    '''
    Tracer
    Track the data in each iteration.
    Note: the chromosome is encoded in to param, which should be flatten.
    '''

    def __init__(self, objective: list):
        self.best_ov = None
        self.iterations = 0
        self.best_param = None
        self.objective_fn = objective

    def track(self, individual: Individual):

        if dominate(individual.ov, self.best_ov):
            self.best_ov = individual.ov
            self.best_param = individual.param
            return True
        return False
