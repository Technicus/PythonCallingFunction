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

    # now get rid of the directory (via basename)
    # then split filename and extension (via splitext)
    #caller_filename_only = os.path.splitext(os.path.basename(caller_filename_full))[0]

    #caller_filename_only = path.splitext(path.filename(caller_filename_full))[0]
    #callingFunction = inspect.stack()[1][3]
    #print('\n< {} : {}() >'.format(callingFile, inspect.stack()[1][3]))
    #f_name, f_ext = path.splitext(path.filename(caller_filename_full))

    # return both filename versions as tuple
    #return caller_filename_full, caller_filename_only
