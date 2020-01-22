#!/usr/bin/env python

import wx # Import WX for ui elements
import logging as log # Import logging library as log in the code
from glob import glob # Import glob for getting filenames
import os # Import os
import yaml # Import yaml so we can use config files
import datetime

import gui.noname as gui # Import our custom gui as gui
import custom_functions # Import our custom files

def return_user_ids():
    userdata_path = os.path.abspath(os.path.join(__file__ ,"..\\userdata\\*"))
    cleaned_ids = []
    raw_ids = ([os.path.basename(x) for x in glob(userdata_path)])
    for id in raw_ids:
        cleaned_ids.append(id.replace(".yaml",""))
    return cleaned_ids

class tshirt_factory(gui.root_frame): # Class for our app frame
    def __init__(self, parent): # Runs once when we init
        gui.root_frame.__init__(self, parent) # Sets root_frame in gui to the init of gui
        
        self.settings_location = "data\\settings.yaml"
        self.userdata_location = "userdata\\"
        self.initalize_filesystem()
        self.timestamp = datetime.datetime.today()

        self.settings = (custom_functions.yaml_loader(self.settings_location)) # Load the yaml settings and save them as self.settings
        self.UserIdComboBox.SetItems(return_user_ids()) # Update with ability to read files in that location
        self.ClothingTypeChoice.SetItems(self.settings["clothing_types"]) # Retreive all the clothing types from settings
        self.ClothingColorChoice.SetItems(self.settings["clothing_colors"]) # Retreive all the clothing colors from settings
        self.DiscountChoice.SetItems(['None']) # Make all new!

    # Function by joe
    def export_all(self, event): # Exports everything at once
        # Capture all variables
        self.user_id = self.UserIdComboBox.GetValue()
        self.clothing_type = self.ClothingTypeChoice.GetStringSelection()
        self.color = self.ClothingColorChoice.GetStringSelection()
        self.base_price = self.BasePriceInput.GetLineText(0)
        self.discount = self.DiscountChoice.GetStringSelection()
        self.use_production_modifiers = self.UseProductionModifiersBox.Get3StateValue()
        self.export_format = self.OutputFormatChoice.GetStringSelection()
        log.debug("Captured all messages.") # Debug message

        # Do all math and logic
        if self.user_id not in return_user_ids():
            custom_functions.yaml_loader(self.userdata_location + str(self.user_id) + ".yaml", {'customer': {'previous_orders': {str(self.timestamp.month) + "-" + str(self.timestamp.day) + "-" + str(self.timestamp.year): {'cost': 30, 'other': 'yote'}}}})

        # Export everything
        if self.export_format == "pdf":
            None
        elif self.export_format == "txt":
            print("this needs to be done")
        else:
            log.error("Error: Export format not understood")
    
    # Function by joe
    def initalize_filesystem(self): # Will reset all settings back to zero
        if not os.path.exists("data\\"): # If the file does not exist, initalize everything
            os.makedirs("data\\")
            os.makedirs("userdata\\")
            custom_functions.yaml_loader(self.settings_location, {'clothing_types': ['T-Shirt', 'Shirt', 'Uniform Shirt', 'Hoodie'], 'clothing_colors': ['Red', 'Green', 'Blue', 'Orange', 'Yellow'], 'production_miltiplers': {'XS': 1.0, 'S': 1.0, 'M': 1.0, 'L': 1.0, 'XL': 1.0, 'XXL': 1.25, 'XXXL': 1.25}})

if __name__ == "__main__":
    log.basicConfig(level=log.DEBUG) # Set logging level
    log.debug("Program Started.") # Debug message

    app = wx.App(redirect=False) # Show console output for errors
    root_window = tshirt_factory(None) # No parent
    root_window.Show() # Show the window
    app.MainLoop() # Run the main GUI loop
