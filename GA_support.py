# !/usr/bin/env python
# --------------------------------------------------------------
# File:          GA_support.py
# Project:       PyEvoAlg
# Created:       Sunday, 8th December 2019 2:13:50 pm
# @Author:       Molin Liu, MSc in Data Science
# Contact:       molin@live.cn
# Last Modified: Sunday, 8th December 2019 2:33:14 pm
# Copyright  © Rockface 2019 - 2020
# --------------------------------------------------------------

from individual import Individual
import numpy as np
from enum import Enum


class Type(Enum):
    MIN = 0
    MAX = 1


def dominate(x: Individual, y: Individual, type='min'):
    '''
    Determine if x dominates y.
    type = [min, max]
    '''
    if type == 'min':
        result = x.ov[:] <= y.ov[:]
    else:
        result = x.ov[:] >= y.ov[:]
    if False in result:
        return False
    return True
