import math
num= 1000000
xarr = []
for i in range(0,num+1):
    xarr.append(2*math.pi/num*i)
yarr = []
for j in xarr:
    yarr.append(abs(math.sin(j)))
print(2*math.pi*sum(yarr)/num)