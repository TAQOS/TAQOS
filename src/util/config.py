###############################################################################
#
#   config.py - A configuration class for holding info about the installation
#               of TAQOS. This information is stored within a persistent
#               SQLite3 DB, as a table of key-value pairs (i.e we have a DB
#               acting as a key-value store, not OP at all)
#   
#   Authors: Aaron Vontell
#   Created on: July 17, 2017
#   Last modified: July 17, 2017
#
###############################################################################

import os.path as op
from os import makedirs, putenv
import sqlite3

this_location = op.dirname(__file__)

class InstallConfig():
    
    def __init__(self):
        self.define_validators()
        self.set_to_default()
    
    def load_from_file(self):
        pass
    
    def get_properties(self):
        """
        Returns a list of the possible properties stored in this configuration
        :return: A list of property keys
        """
        return self.properties.keys()
    
    def get_title(self, key):
        """
        Returns the title or human readable key for this property
        :param key: The property you are trying to access
        :return: The title or human readable key for this property
        """
        return self.properties[key][0]
    
    def get_desc(self, key):
        """
        Returns the description for this property
        :param key: The property you are trying to access
        :return: The description for this property
        """
        return self.properties[key][1]
    
    def get_value(self, key):
        """
        Returns the currently stored value for this property
        :param key: The property you are trying to access
        :return: The value for this property
        """
        return self.properties[key][2]
    
    def is_valid(self, key, val):
        """
        Returns true if val is a valid assignment for the given property
        :param key: The property you are trying to check
        :param val: The value you would like to assign to key
        :return: True if val is valid for the property given by key
        """
        return self.properties[key][3](val)
    
    def set_value(self, key, val):
        """
        Sets the value of the desired property to val
        :param key: The property you are trying to set
        :param val: The value you would like to assign to key
        """
        self.properties[key][2] = val
    
    def save_config(self):
        """
        Saves the configuration file as a SQLite3 DB at the location provided
        through the setup process. This also saves the config file location
        as an environment variable, for later retrieval.
        :return: The location at which this configuration was saved
        """
        
        # Make the directory and DB file
        save_location = self.get_value("save_location")
        config_location = self.get_value("config_location")
        conf_location = save_location + "/" + config_location
        if not op.exists(save_location):
            makedirs(save_location)
        open(conf_location, 'a').close()
        
        # Clear the current contents
        with open(conf_location, "w"):
            pass
        
        # Open a DB connection and save the contents
        conn = sqlite3.connect(conf_location)
        c = conn.cursor()
        
        # Create table for config
        c.execute('''CREATE TABLE config
                     (key text, value text)''')

        # Insert our properties
        # Larger example that inserts many records at a time
        properties = [(prop, self.get_value(prop)) for prop in self.get_properties()]
        c.executemany('INSERT INTO config VALUES (?,?)', properties)

        # Save (commit) the changes
        conn.commit()
        conn.close()
        
        # Save the save_location to an internal file so that we ca reference it
        # later
        desired_folder = this_location + "/../../.data"
        desired_file = desired_folder + "/location.conf"
        if not op.exists(desired_folder):
            makedirs(desired_folder)
        open(desired_file, 'a').close()
        with open(desired_file, "w"):
            pass
        open(desired_file, "w").write(conf_location)
        
        return conf_location
    
    def set_to_default(self):
        """
        Creates a default configuration object, with default property names,
        values, descriptions, and validators. Must only be called after
        define_valicators has been called.
        """
        
        self.properties = {
            "save_location": ["Data save location",
                              "A location to save information used by TAQOS",
                              op.expanduser("~") + "/taqos",
                              self.validators["save_location"]],
            "config_location": ["Config save file",
                                "A file to save the configuration in",
                                "config.db",
                                self.validators["config_location"]]
        }
    
    def define_validators(self):
        """
        Defines validation functions for the properties of the configuration.
        Each function returns true if the property passed is a valid assignment
        """
        
        # Define each validation function
        def _save_location(location):
            return op.isdir(op.expanduser(location))
        
        def _config_location(file_location):
            return True
        
        # Store them within a list
        self.validators = {
            "save_location": _save_location,
            "config_location": _config_location
        }