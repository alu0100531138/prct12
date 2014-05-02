#! /usr/bin/python
import random,sys,os,platform
from math import *

def CPUinfo():
# infofile on Linux machines:
  infofile = '/proc/cpuinfo'
  cpuinfo = {}
  if os.path.isfile(infofile):
    f = open(infofile, 'r')
    for line in f:
     try:
       name, value = [w.strip() for w in line.split(':')]
     except:
       continue
     if name == 'model name':
        cpuinfo['CPU type'] = value
     elif name == 'cache size':
       cpuinfo['cache size'] = value
     elif name == 'cpu MHz':
       cpuinfo['CPU speed'] = value + ' Hz'
     elif name == 'vendor_id':
       cpuinfo['vendor ID'] = value
    f.close()
  return cpuinfo
  
if __name__ == '__main__':
  print CPUinfo()
  print 'Inserte el nombre del fichero donde guardar la informacion'
  fich = raw_input(str)
  f = open(fich,'w') 
  f.write('{0}\n'.format(CPUinfo()))
  f.write('{0}\n'.format(platform.uname()))
  f.write('{0}\n'.format(platform.platform()))
  f.write('{0}\n'.format(platform.python_version()))
  f.write('{0}\n'.format(platform.python_build()))
  f.close()