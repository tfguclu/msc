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

for file in os.listdir('.'):
    if fnmatch.fnmatch(file, '*.eda.npz'):
        file_names_sorted.append(file)
        file_names_sorted = sorted(file_names_sorted, key=str.lower)
        model_file = file
        loaded_file = loadModel(str(file))
        file_names[str(file)] = loaded_file[0]
range_file_number = len(file_names_sorted)

for a in range(range_file_number):
    for b in range(range_file_number):
        comparison_matrix[a,b] = calcOverlap(file_names[file_names_sorted[a]],file_names[file_names_sorted[b]])


# for i in range(63):
#     for j in range(63):
#         comparison_matrix[i,j] = calcOverlap(
#             file_names.values()[i], file_names.values()[j]
# )

np.savetxt("comparison_matrix.dat",comparison_matrix)

# for a in range(63):
#     print(file_names.keys()[a])