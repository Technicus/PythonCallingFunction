# Callee.py

#from inspect import currentframe, stack
from inspect import stack
from os import path

def get_caller_info():
    # first get the full filename (including path and file extension)
    callee_frame = stack()[0]
    caller_frame = stack()[1]
    caller_filename_full = caller_frame.filename

    print("\nstack()[0]._fields\n  {}\n".format(stack()[0]._fields))

    print("stack()[0]")
    for a in range(len(stack()[0])):
        print ("  {} : {} : {}".format(a, stack()[0][a].__class__.__name__, stack()[0][a]))
    print()

    print("stack()[1]")
    for y in range(len(stack()[1])):
        print ("  {} : {} : {}".format(y, stack()[1][y].__class__.__name__, stack()[1][y]))
    print()

    # return both filename versions as tuple
    #return caller_filename_full, caller_filename_only
