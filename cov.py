#!/usr/bin/env python

filename = raw_input('Enter a file name: ')

from prody import *
from pylab import *
import numpy

system = parsePDB(str(filename)+".pdb")

traj = DCDFile(str(filename)+".dcd")

traj.link(system)

frames1 = traj[5010:15010]
frames2 = traj[15010:25010]

eda1 = EDA('')
eda2 = EDA('')

eda1.buildCovariance(frames1)
eda2.buildCovariance(frames2)

eda1.calcModes(10000)
eda2.calcModes(10000)

saveModel(eda1,str(filename)+"_10_30")
saveModel(eda2,str(filename)+"_30_50")

writeNMD(str(filename)+"_10_30", eda1, system)
writeNMD(str(filename)+"_30_50", eda2, system)



import matplotlib.pyplot as plt
arange = np.arange(eda1.numAtoms())
cross_correlations = np.zeros((arange[-1]+2, arange[-1]+2))
cross_correlations[arange[0]+1:,arange[0]+1:] = calcCrossCorr(eda1)
plt.imshow(cross_correlations), plt.colorbar()
plt.axis([arange[0]+0.5, arange[-1]+1.5, arange[0]+0.5, arange[-1]+1.5])
savefig("cc_"+str(filename)+"_10_30", dpi=300, bbox_inches='tight')

plt.clf()
plt.close()

import matplotlib.pyplot as plt
arange = np.arange(eda2.numAtoms())
cross_correlations = np.zeros((arange[-1]+2, arange[-1]+2))
cross_correlations[arange[0]+1:,arange[0]+1:] = calcCrossCorr(eda2)
plt.imshow(cross_correlations), plt.colorbar()
plt.axis([arange[0]+0.5, arange[-1]+1.5, arange[0]+0.5, arange[-1]+1.5])
savefig("cc_"+str(filename)+"_30_50", dpi=300, bbox_inches='tight')



