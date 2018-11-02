import matplotlib.pyplot as  plt
import numpy as  np
plt.figure()
plt.xlim((0,5))
plt.ylim((0,5))
x1=input("x1=")
y1=input("y1=")
x2=input("x2=")
y2=input("y2=")
x1=int(x1)
y1=int(y1)
x2=int(x2)
y2=int(y2)
x=x1+x2
y=y1+y2
plt.scatter(x1,y1)
plt.scatter(x2,y2)
plt.scatter(x,y)
plt.show()