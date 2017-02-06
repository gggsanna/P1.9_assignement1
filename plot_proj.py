import sys
import numpy as np
import matplotlib.pyplot as plt

available_functions={ 1: ("x -> x", lambda x: x),
                      2: ("x -> x^2", lambda x: x*x),
                      3: ("x -> x^3", lambda x: x*x*x),
                      4: ("x -> sin(x)", lambda x: np.sin(x)),
                      5: ("x -> cos(x)", lambda x: np.cos(x)),
                      6: ("x -> tan(x)", lambda x: np.tan(x)),
                      7: ("x -> exp(x)", lambda x: np.exp(x)),
                      8: ("x -> sqrt(|x|)", lambda x: np.sqrt(abs(x)))
                      }

# print Usage if no input is provided
usage_message="Usage: python " + str(sys.argv[0]) + " <n> \n" \
             + "\"n\" is an integer. The function corresponding to it is:"
if(len(sys.argv) == 1):
    print usage_message
    for key in available_functions:
        print str(key) + ": " + available_functions[key][0]
    sys.exit()

# set f according to input
f = available_functions[int(sys.argv[1])][1]

# Test handling command line input
# test_val = 10
# print "The identity function in " + str(test_val) + " is: " + str(f(10))

# setup x and y axes
start=-3.0
end=3.0
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
