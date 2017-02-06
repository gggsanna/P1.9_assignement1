import sys
import numpy as np
import matplotlib.pyplot as plt

available_functions={ 1: ("x -> x", lambda x: x),
                      2: ("x -> sin(x)", lambda x: np.sin(x)),
                      3: ("x -> cos(x)", lambda x: np.cos(x)),
                      4: ("x -> tan(x)", lambda x: np.tan(x))
                      }

# set f according to input
f = available_functions[int(sys.argv[1])][1]

# Test handling command line input
# test_val = 10
# print "The identity function in " + str(test_val) + " is: " + str(f(10))

# setup x and y axes
start=-5.0
end=5.0
interval=0.1
nsteps=(end-start + 0.0)/interval + 1
# abs((nsteps-1)*interval-(end-start))<tol
xval=np.linspace(start,end,nsteps)
yval=f(xval)

# Test creation of xval and yval
# print xval[10:20], yval[10:20]

# plot function
plt.plot(xval,yval)
plt.show()
