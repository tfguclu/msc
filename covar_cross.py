#!/usr/bin/env python

from prody import *
from pylab import *
import numpy as np
from os.path import basename
import fnmatch
import os
from os import *

chunk_start = 5010
chunk_end = 25010
ref_frame = chunk_start
file_suffix = "_10_50"

for file in os.listdir('.'):
    if fnmatch.fnmatch(file, '*.pdb'):
        pdb = file

for file in os.listdir('.'):
    if fnmatch.fnmatch(file, '*.dcd'):
        dcd = file

system = parsePDB(str(pdb))

traj = DCDFile(str(dcd))

traj.link(system)

frames = traj[int(chunk_start):int(chunk_end)]

refFrame = traj[int(ref_frame)]

frames.setCoords(refFrame.getCoords())

frames.superpose()

eda = EDA('')

eda.buildCovariance(frames)

covariance = eda.getCovariance()
cross_corr = np.zeros((159,159))
for i in range(159):
    for j in range(159):
        a = (3*(i))
        b = (3*(i)+1)
        c = (3*(i)+2)
        d = (3*(j))
        e = (3*(j)+1)
        f = (3*(j)+2)
        cross_corr[i,j] = covariance[a,d]+covariance[b,e]+covariance[c,f]

np.savetxt('cross_corr_'+str(os.path.splitext(dcd)[0])+str(file_suffix)+'.dat', cross_corr, fmt='%8.10f')
np.savetxt('covariance_'+str(os.path.splitext(dcd)[0])+str(file_suffix)+'.dat', covariance, fmt='%8.10f')

eda.calcModes(10000)

saveModel(eda,str(os.path.splitext(dcd)[0])+str(file_suffix))

writeNMD(str(os.path.splitext(dcd)[0])+str(file_suffix), eda, system)

import matplotlib.pyplot as plt
arange = np.arange(eda.numAtoms())
cross_correlations = np.zeros((arange[-1]+2, arange[-1]+2))
cross_correlations[arange[0]+1:,arange[0]+1:] = cross_corr
plt.imshow(cross_correlations,vmin=-1,vmax=1), plt.colorbar()
plt.axis([arange[0]+0.5, arange[-1]+1.5, arange[0]+0.5, arange[-1]+1.5])
savefig("cc_"+str(os.path.splitext(dcd)[0])+str(file_suffix), dpi=300, bbox_inches='tight')

plt.clf()
plt.close()

print("chunk start "+str(chunk_start)+" "+"chunk end "+str(chunk_end)+" "+"ref frame "+str(ref_frame))