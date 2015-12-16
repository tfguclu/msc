#!/usr/bin/env python

from prody import *
from pylab import *
import numpy as np
from os.path import basename
import fnmatch
import os


def filter_cov(model_file, mod):
    """ filtering covariance matrix by mode"""
    loaded_model = loadModel(str(model_file))
    cov_mat = loaded_model.getCovariance()
    mode_eigenvector = loaded_model[int(mod)].getEigvec()
    filtered_cov_mat = cov_mat * mode_eigenvector
    return filtered_cov_mat

for file in os.listdir('.'):
    if fnmatch.fnmatch(file, '*.eda.npz'):
        filtered_covar_mat = filter_cov(file, 0)
        filtered_cross_corr = np.zeros((159,159))
        for i in range(159):
            for j in range(159):
                a = (3*(i))
                b = (3*(i)+1)
                c = (3*(i)+2)
                d = (3*(j))
                e = (3*(j)+1)
                f = (3*(j)+2)
                filtered_cross_corr[i,j] = filtered_covar_mat[a,d]+filtered_covar_mat[b,e]+filtered_covar_mat[c,f]
        np.savetxt(str(os.path.splitext(file)[0]) + "_mod0_filtered_cov_mat.dat", filtered_covar_mat)
        np.savetxt(str(os.path.splitext(file)[0]) + "_mod0_filtered_corr_mat.dat", filtered_cross_corr)
