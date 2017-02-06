import sys

available_functions={ 1: ("x -> x", lambda x: x)
                      }

# set f according to input
f = available_functions[int(sys.argv[1])][1]

# Test handling command line input
# test_val = 10
# print "The identity function in " + str(test_val) + " is: " + str(f(10))
