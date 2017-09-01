###############################################################################
#
#   salsa.py - A command for quitting the TAQOS REPL
#   
#   Authors: Aaron Vontell
#   Created on: July 22, 2017
#   Last modified: July 22, 2017
#
###############################################################################

from salsa import BaseCommand, CommandResponse

class QuitCommand(BaseCommand):
    
    @staticmethod
    def process(args):
        return CommandResponse.createQuit()