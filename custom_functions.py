#!/usr/bin/env python

import logging as log # Import logging library as log in the code
from glob import glob # Import glob for getting filenames
import os # Import os
import yaml # Import yaml so we can use config files
import datetime


# Function by Nathan
def return_dollar(dollar_value):
    return "$" + str(dollar_value) # Concanate strings

# Function By Joe
def yaml_loader(fileDir, data = None):
    if data != None:
        # Write YAML file
        with open(fileDir, "w+") as outfile:
            yaml.dump(data, outfile)

    # Read YAML file
    with open(fileDir, 'r') as stream:
        return yaml.safe_load(stream)
