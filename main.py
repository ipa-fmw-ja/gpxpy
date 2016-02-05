#!/usr/bin/env python

from Tkinter import Tk
from tkFileDialog import askopenfilename
import numpy as np


from gpxpy.parser import *
Tk().withdraw()
filename = askopenfilename()
print filename

with open(filename, "r") as f:
    gpx_xml = f.read()

parser = GPXParser(gpx_xml)
gpx = parser.parse()
#print gpx.to_xml()

#print gpx.tracks[0].to_xml()
track_0=gpx.tracks[0]
trkpts=track_0.segments[0].points
#print trkpts
distance = []
for i,point in enumerate(trkpts):
    if i-1<0:
        distance.append(point.distance(trkpts[0]))
    else:
        distance.append(point.distance(trkpts[i-1])+distance[-1])

#distance= np.ndarray(distance).cumsum()
print distance[-1]
print len(distance)
