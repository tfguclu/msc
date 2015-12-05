#!/usr/bin/env python

import sys
import numpy as np
import argparse


parser = argparse.ArgumentParser(description="Calculate the dot\
 product of two covariance matrices")
parser.add_argument('cov1', type=str, nargs=1, help='First\
 Covariance matrix dat file')
parser.add_argument('cov2', type=str, nargs=1, help='Second\
 Covariance matrix dat file')
args = parser.parse_args()


def dot_product(cov1, cov2):
    """ dot product between covariance matrices"""

    cov1 = np.loadtxt(cov1)
    cov2 = np.loadtxt(cov2)
    mag_cov1 = np.linalg.norm(cov1)
    mag_cov2 = np.linalg.norm(cov2)
    dot_prdct = ((cov1*cov2)/(mag_cov1*mag_cov2)).sum()
    return dot_prdct

print(dot_product(args.cov1[0], args.cov2[0]))
