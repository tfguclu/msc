#!/usr/bin/env python

from prody import *
from pylab import *
import numpy as np
from os.path import basename
import fnmatch
import os
from os import *

comparison_matrix = np.zeros((63, 63))
file_names = {}
file_names_sorted = []

def dot_product(cov1, cov2):
    """ dot product between covariance matrices"""

    cov1 = np.loadtxt(cov1)
    cov2 = np.loadtxt(cov2)
    mag_cov1 = np.linalg.norm(cov1)
    mag_cov2 = np.linalg.norm(cov2)
    dot_prdct = ((cov1*cov2)/(mag_cov1*mag_cov2)).sum()
    return dot_prdct

for file in os.listdir('.'):
    if fnmatch.fnmatch(file, '*.dat'):
        file_names_sorted.append(file)
        file_names_sorted = sorted(file_names_sorted, key=str.lower)
        #model_file = file
        #loaded_file = loadModel(str(file))
        #file_names[str(file)] = loaded_file[0]
range_file_number = len(file_names_sorted)

for a in range(range_file_number):
    for b in range(range_file_number):
        comparison_matrix[a, b] = dot_product(
            file_names_sorted[a], file_names_sorted[b])


# for i in range(63):
#     for j in range(63):
#         comparison_matrix[i,j] = calcOverlap(
#             file_names.values()[i], file_names.values()[j]
# )

np.savetxt("comparison_matrix_of_dotproduct.dat", comparison_matrix)

f = open('files_sorted_list.dat', 'w')
f.write(file_names_sorted)
f.close()

# for a in range(63):
#     print(file_names.keys()[a])