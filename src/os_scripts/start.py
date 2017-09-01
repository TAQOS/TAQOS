###############################################################################
#
#   start.py - Script for starting up the TAQOS interface
#   
#   Authors: Aaron Vontell
#   Created on: July 13, 2017
#   Last modified: July 13, 2017
#
###############################################################################

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from taqos.runner.shell import start_repl

start_repl()
