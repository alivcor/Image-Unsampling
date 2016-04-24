import numpy as np
import scipy.ndimage
import re
from numpy import array
x = raw_input()
x1 = x.split( )
r = int(x1[0])
c = int(x1[1])
s = int(x1[2])
y = raw_input()
y1 = y.split( )
r0 = int(y1[0])
c0 = int(y1[1])
redval=""
grval=""
blval=""
rednewmatrix=list()
grnewmatrix=list()
blnewmatrix=list()
rednewrow=list()
blnewrow=list()
grnewrow=list()
for i in range(0,r):
    row = raw_input()
    values = row.split( )
    for val in values:
        mobj = re.match(r'(\d+)(\,)(\d+)(\,)(\d+)',val)
        blval = int(mobj.group(1))
        grval = int(mobj.group(3))
        redval = int(mobj.group(5))
        rednewrow.append(redval)
        grnewrow.append(grval)
        blnewrow.append(blval)
    rednewmatrix.append(rednewrow)
    blnewmatrix.append(blnewrow)
    grnewmatrix.append(grnewrow)
    rednewrow=list()
    blnewrow=list()
    grnewrow=list()



redfinal = scipy.ndimage.zoom(array(rednewmatrix), s, order=1)
greenfinal = scipy.ndimage.zoom(array(grnewmatrix), s, order=1)
bluefinal = scipy.ndimage.zoom(array(blnewmatrix), s, order=1)

for i in range(0,r0):
    for j in range(0,c0):
        truffle = str(bluefinal[i,j])+","+str(greenfinal[i,j])+","+str(redfinal[i,j])
        print(truffle),
    print("")

