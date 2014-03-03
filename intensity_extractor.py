#!/usr/bin/env python
 
import csv
import sys
import numpy as np
import scipy as sp
import platform

sys.stderr.write('python version ' + platform.python_version() + '\n')

def value_extractor(infile):
    with open(infile, 'rb') as f:
        print "opened handel"
        for lines in xrange(32):
            next(f)
        intensity = []
        corr_intensity = []
        print_control = []
        reader = csv.reader(f, delimiter = '\t')
        print "Block\tRow\tMean\tSt_Dev\tCV"
        for row in reader:
            #make all strings to int
            row = map(int, row)
            intensity.append(row[6])
                #if four elements have been added to the list it removes the backgrounf and calculates the mean. The lists are reset
            if len(intensity) == 4:
                corr_intensity = np.array(intensity)
                mean = np.mean(corr_intensity)
                stdev = np.std(corr_intensity)
                cv = stdev/mean * 100 
                print row[0], '\t', row[2], '\t', mean, '\t', round(stdev, 1), '\t', round(cv, 1)
                # each block is a key to a list of means for that block 
                corr_intensity = []
                intensity = []
    return(intensity)

infile = sys.argv[1]
value_extractor(infile)

#sys.stderr.write(print_control)