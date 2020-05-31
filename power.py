#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 27 22:24:12 2020

@author: kevinrojas
"""


# calculate power curves for varying sample and effect size
from numpy import array
from matplotlib import pyplot
from statsmodels.stats.power import TTestIndPower

# parameters for power analysis
effect_sizes = array([0.25, 0.5, 0.75])
sample_sizes = array(range(5, 100))
# calculate power curves from multiple power analyses
analysis = TTestIndPower()
analysis.plot_power(dep_var='nobs', nobs=sample_sizes, effect_size=effect_sizes)
pyplot.show()



for i in effect_sizes:
    # estimate sample size via power analysis
    # parameters for power analysis
    effect = i
    alpha = 0.05
    power = 0.5
    # perform power analysis
    analysis = TTestIndPower()
    result = analysis.solve_power(effect, power=power, nobs1=None, ratio=1.0, alpha=alpha)
    print("Con un efecto de:", i)
    print('Sample Size: %.3f' % result)