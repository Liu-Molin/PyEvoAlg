# !/usr/bin/env python
# --------------------------------------------------------------
# File:          plot.py
# Project:       PyEvoAlg
# Created:       Tuesday, 10th December 2019 7:37:45 pm
# @Author:       Molin Liu, MSc in Data Science
# Contact:       molin@live.cn
# Last Modified: Tuesday, 10th December 2019 7:37:47 pm
# Copyright  © Rockface 2019 - 2020
# --------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np


def loss(loss_value, iterations):
    '''
    Plot loss function 
    '''
    fig, ax = plt.subplot()
    ax.plot(loss_value, iterations, color='tab:orange')
