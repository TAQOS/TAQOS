###############################################################################
#
#   salsa.py - A command resolver, where the commands are located within the
#              salsa module
#   
#   Authors: Aaron Vontell
#   Created on: July 21, 2017
#   Last modified: July 22, 2017
#
###############################################################################

from abc import ABCMeta, abstractmethod
import importlib
import imp
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
SPICES = [f.split(".py")[0] for f in os.listdir(dir_path) if f.endswith('.py') and f != "__init__.py" and f != "salsa.py"]

class BaseCommand:
    """
    An abstract class which represents a basic command to be executed.
    Subclasses must defined a process() method which takes in a string
    to be executed (which are the arguments of the class) and executes
    the command.
    """
    
    __metaclass__ = ABCMeta
    
    @abstractmethod
    @staticmethod
    def process(command):
        """
        Process the given command, which does not include the command-word
        that was used to reach this command (i.e. run example.py --> example.py).
        Return None if the REPL should not print anything else after execution, or
        return a CommandResponse instance. Feel free to print during this execution.
        """
        pass
    
    
class CommandResponse:
    """
    Represents a response to handle on the REPL regarding a command. Currently
    supported commands are None, Quit, Failed, Success
    """
    
    @staticmethod
    def createNone():
        """
        Creates a response which indicates that the REPL should not do anything
        special after the command has been processed.
        :return: A dictionary representing this response
        """
        return {"type": "none"}
    
    @staticmethod
    def createQuit():
        """
        Creates a response which indicates that the REPL should quit after
        the command has be processed.
        :return: A dictionary representing this response
        """
        return {"type": "quit"}
    
    @staticmethod
    def createFailed(message=None):
        """
        Creates a response which indicates that the REPL should print a
        failure regarding the command. If message is None, then no extra
        information should be printed.
        :param message: A message to print, or None if no message should be
                        printed. Defaults to None.
        :return: A dictionary representing this response
        """
        return {"type": "fail", "message": message}
    
    @staticmethod
    def createSuccess(message=None):
        """
        Creates a response which indicates that the REPL should print a
        success regarding the command. If message is None, then no extra
        information should be printed.
        :param message: A message to print, or None if no message should be
                        printed. Defaults to None.
        :return: A dictionary representing this response
        """
        return {"type": "success", "message": message}
    
    
class CommandResolver:
    """
    Resolves and executes commands from the REPL by searching through the
    available commands in the "salsa" module.
    """
    
    @staticmethod
    def process(command):
        """
        Processes and executes the given command.
        :param command: The full command to execute
        :return: A CommandResponse object
        """
        
        command = command.split(" ")[0]
        if command in SPICES:
            module = importlib.import_module("salsa")
            print(module)
            return CommandResponse.createQuit()
        else:
            return CommandResponse.createFailed("Command '%s' not found." % command)