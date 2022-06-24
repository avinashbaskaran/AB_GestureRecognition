import numpy as np
import os, getpass
from os.path import join, getsize

user = 'Copy of ' + getpass.getuser()
path = "C://Documents and Settings" + user + "./"
folderCounter = sum([len(folder) for r,d,folder in os.walk(path)])
fileCounter = sum([len(files) for r, d, files in os.walk(path)])

print
#filename = 
#data = np.loadtxt(filename, delimiter=',', skiprows=1, dtype=str)