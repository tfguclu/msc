#!/usr/bin/env python

from pylab import *
from prody import *
import sys


pdb = str(raw_input('pdb name'))+".pdb"

dcdname = str(raw_input('dcd name'))

dcd = dcdname+".dcd"

system = parsePDB(pdb)
traj = Trajectory(dcd)

traj.link(system)

refFrame = traj[5009]

frames1 = traj[5010:15010]
frames2 = traj[15010:25010]

frames1.setCoords(refFrame.getCoords())
frames2.setCoords(refFrame.getCoords())

frames1.superpose()
frames2.superpose()

RMSF1 = frames1.getRMSFs()

out_file1 = str(dcdname+"_rmsf_10_30.dat")

f1 = open(out_file1, 'w')

for i in range(159):
	f1.write('%g\n' % (RMSF1[i]))
f1.close()

RMSF2 = frames2.getRMSFs()

out_file2 = str(dcdname+"_rmsf_30_50.dat")

f2 = open(out_file2, 'w')

for i in range(159):
	f2.write('%g\n' % (RMSF2[i]))
f2.close()

