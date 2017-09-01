###############################################################################
#
#   setup.py - Script for the initial setup of TAQOS
#   
#   Authors: Aaron Vontell
#   Created on: July 13, 2017
#   Last modified: July 17, 2017
#
###############################################################################

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
import util.tlog as logger
from util.config import InstallConfig

# Information for the storage of data used by TAQOS will be gathered by the
# user here. The user can either provide a configuration file, or enter the
# information automatically.

def setup_through_input(config):
    """
    Completes setup of TAQOS by asking the user for input.
    """
    
    print("TAQOS Manual Setup")
    props = config.get_properties()
    while len(props) > 0:
        prop = props.pop(0)
        result = raw_input("> " + config.get_title(prop) + " (" + config.get_value(prop) + "): ")
        if len(result) == 0:
            continue
        elif config.is_valid(prop, result):
            config.set_value(prop, result)
        else:
            props.insert(0, prop)
            
    config_save = config.save_config()
    print("Configuration has been saved in %s" % config_save)

def setup_through_config(config):
    """
    Completes the setup of TAQOS through the use of a configuration file. If an
    input is missing, the default value will be used.
    :param config: An absolute path to a configuration file for setting
                   up TAQOS.
    """
    
    pass

def start_setup(config_location=None):
    """
    Starts the setup process, given an optional configuration file.
    :param config_location: An optional absolute path to a configuration file 
                            for setting up TAQOS. Defaults to None, which moves
                            onto manual setup.
    """
    
    print("Welcome to the TAQOS installation program (v0.0.1)")
    print("More info about TAQOS can be found at http://taqos.io")
    print("----------------------------------------------------------------\n")
    
    config = InstallConfig()
    
    if config_location:
        setup_through_config(config)
    else:
        setup_through_input(config)

start_setup()