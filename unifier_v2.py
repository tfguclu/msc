#!/usr/bin/env python

# filename = raw_input('Enter a file name: ')

from prody import *
from pylab import *
import numpy
from os.path import basename
import fnmatch
import os
from os import *

for file in os.listdir('.'):
    if fnmatch.fnmatch(file, '*.pdb'):
        pdb = file

for file in os.listdir('.'):
    if fnmatch.fnmatch(file, '*.dcd'):
        dcd = file

system = parsePDB(str(pdb))

traj = DCDFile(str(dcd))

traj.link(system)

frames1 = traj[5010:25010]

eda1 = EDA('')

eda1.buildCovariance(frames1)
# eda2.buildCovariance(frames2)

eda1.calcModes(10000)
#eda2.calcModes(10000)

saveModel(eda1,str(os.path.splitext(dcd)[0])+"_10_50")
#saveModel(eda2,str(filename)+"_30_50")

writeNMD(str(os.path.splitext(dcd)[0])+"_10_50", eda1, system)
#writeNMD(str(filename)+"_30_50", eda2, system)



import matplotlib.pyplot as plt
arange = np.arange(eda1.numAtoms())
cross_correlations = np.zeros((arange[-1]+2, arange[-1]+2))
cross_correlations[arange[0]+1:, arange[0]+1:] = calcCrossCorr(eda1)
plt.imshow(cross_correlations), plt.colorbar()
plt.axis([arange[0]+0.5, arange[-1]+1.5, arange[0]+0.5, arange[-1]+1.5])
savefig("cc_"+str(os.path.splitext(dcd)[0])+"_10_50", dpi=300,
        bbox_inches='tight')

#print basename("/a/b/c.txt")
#plt.clf()
#plt.close()

#import matplotlib.pyplot as plt
#arange = np.arange(eda2.numAtoms())
#cross_correlations = np.zeros((arange[-1]+2, arange[-1]+2))
#cross_correlations[arange[0]+1:,arange[0]+1:] = calcCrossCorr(eda2)
#plt.imshow(cross_correlations), plt.colorbar()
#plt.axis([arange[0]+0.5, arange[-1]+1.5, arange[0]+0.5, arange[-1]+1.5])
#savefig("cc_"+str(filename)+"_30_50", dpi=300, bbox_inches='tight')



