#!/usr/bin/env python

from prody import *
from pylab import *
import numpy as np
from os.path import basename
import fnmatch
import os
#from os import *

file_names_sorted = []


def contribution_calc(model_file):
    """ dot product between covariance matrices"""
    global contri_list, sum_eigvals
    contri_list = []
    loaded_model = loadModel(str(model_file))
    sum_eigvals = 0
    for i in range(471):
        sum_eigvals += loaded_model[i].getEigval()
    contri1 = (loaded_model[0].getEigval()/sum_eigvals)*100
#    contri_list.append(contri1)
    contri2 = (loaded_model[1].getEigval()/sum_eigvals)*100
#    contri_list.append(contri2)
    contri3 = (loaded_model[2].getEigval()/sum_eigvals)*100
    contri_list.extend((contri1, contri2, contri3))
    return contri_list

for file in os.listdir('.'):
    if fnmatch.fnmatch(file, '*.eda.npz'):
        file_names_sorted.append(file)
        file_names_sorted = sorted(file_names_sorted, key=str.lower)
range_file_number = len(file_names_sorted)

f = open("contribution_results.dat", 'w')
for a in range(range_file_number):
    mf = contribution_calc(str(file_names_sorted[a]))
    f.write ("%s\t%d\t%d\t%d\n" % (str(file_names_sorted[a]), contri_list[0], contri_list[1], contri_list[2]))
    # for b in range(range_file_number):
    #     comparison_matrix[a, b] = dot_product(
    #         file_names_sorted[a], file_names_sorted[b])
f.close()



# np.savetxt("mod_contribution.dat", comparison_matrix)


# for a in range(63):
#     print(file_names.keys()[a])