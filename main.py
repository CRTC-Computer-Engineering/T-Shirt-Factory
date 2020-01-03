#!/usr/bin/env python

import wx # Import WX for ui elements
import logging as log # Import logging library as log in the code
import gui.noname as gui # Import our custom gui as gui
from glob import glob # Import glob for getting filenames
import os # Import os
import yaml # Import yaml so we can use config files


def return_user_ids():
    userdata_path = os.path.abspath(os.path.join(__file__ ,"..\\userdata\\*"))
    cleaned_ids = ([os.path.basename(x) for x in glob(userdata_path)])
    return cleaned_ids
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

class tshirt_factory(gui.root_frame): # Class for our app frame
    def __init__(self, parent): # Runs once when we init
        gui.root_frame.__init__(self, parent) # Sets root_frame in gui to the init of gui
        
        self.settings_location = "data\\settings.yaml"
        self.initalize_filesystem()

        self.settings = (yaml_loader(self.settings_location)) # Load the yaml settings and save them as self.settings
        self.UserIdComboBox.SetItems(['0001', '0002', '0003']) # Make all new!
        self.ClothingTypeChoice.SetItems(self.settings["clothing_types"]) # Retreive all the clothing types from settings
        self.ClothingColorChoice.SetItems(self.settings["clothing_colors"]) # Retreive all the clothing colors from settings
        self.DiscountChoice.SetItems(['None', 'Blue', 'Nathan Hewy']) # Make all new!

    # Function by joe
    def export_all(self, event): # Exports everything at once
        # Capture all variables
        self.user_id = self.UserIdComboBox.GetCurrentSelection()
        self.clothing_type = self.ClothingTypeChoice.GetCurrentSelection()
        self.color = self.ClothingColorChoice.GetCurrentSelection()
        self.base_price = self.BasePriceInput.GetLineText(0)
        self.discount = self.DiscountChoice.GetCurrentSelection()
        self.use_production_modifiers = self.UseProductionModifiersBox.Get3StateValue()
        log.debug("Ran export all.") # Debug message
    
    # Function by joe
    def initalize_filesystem(self): # Will reset all settings back to zero
        if not os.path.exists("data\\"): # If the file does not exist, initalize everything
            os.makedirs("data\\")
            yaml_loader(self.settings_location, {'clothing_types': ['T-Shirt', 'Shirt', 'Uniform Shirt', 'Hoodie'], 'clothing_colors': ['Red', 'Green', 'Blue', 'Orange', 'Yellow'], 'production_miltiplers': {'XS': 1.0, 'S': 1.0, 'M': 1.0, 'L': 1.0, 'XL': 1.0, 'XXL': 1.25, 'XXXL': 1.25}})

if __name__ == "__main__":
    log.basicConfig(level=log.DEBUG) # Set logging level
    log.debug("Program Started.") # Debug message

    app = wx.App(redirect=False) # Show console output for errors
    root_window = tshirt_factory(None) # No parent
    root_window.Show() # Show the window
    app.MainLoop() # Run the main GUI loop
