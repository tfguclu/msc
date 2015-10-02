#!/usr/bin/env python

from prody import *
from pylab import *
import numpy
from os.path import basename
import fnmatch
import os
from os import *
import matplotlib.pyplot as plt

reference_eda = loadModel('1rx2_ndph_dhf_calpha_50_90.eda.npz')
reference_modes = reference_eda[:5]

for file in os.listdir('.'):
    if fnmatch.fnmatch(file, '*dhf*.eda.npz'):
        compared_eda_file = file
        compared_eda = loadModel(str(compared_eda_file))
        compared_modes = compared_eda[:5]
        overlap = abs(calcOverlap(reference_modes, compared_modes))
        if overlap.ndim == 0:
            overlap = np.array([[overlap]])
        elif overlap.ndim == 1:
            overlap = overlap.reshape((reference_modes.numModes(), compared_modes.numModes()))
        cmap = plt.cm.jet
        norm = plt.normalize(0, 1)
        show = (plt.pcolor(overlap, cmap=cmap, norm=norm), plt.colorbar())
        x_range = np.arange(1, compared_modes.numModes() + 1)
        plt.xticks(x_range-0.5, x_range)
        y_range = np.arange(1, reference_modes.numModes() + 1)
        plt.yticks(y_range-0.5, y_range)
        plt.axis([0, compared_modes.numModes(), 0, reference_modes.numModes()])
        savefig("mode_overlap_"+str(basename(compared_eda_file)).split('.')[0], dpi=300, bbox_inches='tight')
        plt.clf()
        plt.close()

