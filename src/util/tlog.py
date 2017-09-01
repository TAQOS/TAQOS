###############################################################################
#
#   tlog.py - Methods and constants for pretty printing to the console
#   
#   Authors: Aaron Vontell
#   Created on: July 13, 2017
#   Last modified: July 13, 2017
#
###############################################################################

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
def print_blue(string):
    print(bcolors.OKBLUE + string + bcolors.ENDC)