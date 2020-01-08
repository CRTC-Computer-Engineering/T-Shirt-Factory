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

class shirt():
    def __init__(self, qty, base_cost, fee, name):
        self.qty = int(qty)
        self.base_cost = float(base_cost)
        self.fee = float(fee)
        self.name = name

    def get_invoice_text(self):
        if self.fee == 0:
            return(str(self.qty) + " " + self.name + "s")
        else:
            return(str(self.qty) + " " + self.name + "s  with a $" + str(self.fee) + " fee per " + self.name)
    def get_cost(self):
        return self.qty * (self.base_cost + self.fee)

class tshirt_factory(gui.root_frame): # Class for our app frame
    def __init__(self, parent): # Runs once when we init
        gui.root_frame.__init__(self, parent) # Sets root_frame in gui to the init of gui
        
        self.settings_location = "data\\settings.yaml"
        self.userdata_location = "userdata\\"
        self.initalize_filesystem()

        self.settings = (custom_functions.yaml_loader(self.settings_location)) # Load the yaml settings and save them as self.settings
        self.UserIdComboBox.SetItems(return_user_ids()) # Update with ability to read files in that location
        self.ClothingTypeChoice.SetItems(self.settings["clothing_types"]) # Retreive all the clothing types from settings
        self.ClothingColorChoice.SetItems(self.settings["clothing_colors"]) # Retreive all the clothing colors from settings
        self.DiscountChoice.SetItems(['None']) # Make all new!

    # Function by joe
    def exit(self, event):
        exit()

    # Function by joe
    def export_all(self, event): # Exports everything at once
        self.user_id = self.UserIdComboBox.GetValue() # Capture the User ID
        self.clothing_type = self.ClothingTypeChoice.GetStringSelection() # Capture the Clothing Type
        self.color = self.ClothingColorChoice.GetValue() # Capture the Color Selection
        self.base_price = self.BasePriceInput.GetLineText(0) # Capture the Base Price
        self.discount = self.DiscountChoice.GetStringSelection() # Capture the discount choice
        self.use_production_modifiers = self.UseProductionModifiersBox.Get3StateValue() # Capture the bool
        self.export_format = self.OutputFormatChoice.GetStringSelection() # Capture the output format
        log.debug("Captured all settings.") # Debug message

        self.SShirt = shirt(self.SSpin.GetValue(), self.base_price, self.settings["production_miltiplers"]["S"], "S " + self.clothing_type) # Get the values of all the spinboxes for the qty of shirts
        self.MShirt = shirt(self.MSpin.GetValue(), self.base_price, self.settings["production_miltiplers"]["M"], "M " + self.clothing_type)
        self.LShirt = shirt(self.LSpin.GetValue(), self.base_price, self.settings["production_miltiplers"]["L"], "L " + self.clothing_type)
        self.XLShirt = shirt(self.XLSpin.GetValue(), self.base_price, self.settings["production_miltiplers"]["XL"], "XL " + self.clothing_type)
        self.XXLShirt = shirt(self.XXLSpin.GetValue(), self.base_price, self.settings["production_miltiplers"]["XXL"], "XXL " + self.clothing_type)
        self.XXXLShirt = shirt(self.XXXLSpin.GetValue(), self.base_price, self.settings["production_miltiplers"]["XXXL"], "XXXL " + self.clothing_type)
        self.XXXXLShirt = shirt(self.XXXXLSpin.GetValue(), self.base_price, self.settings["production_miltiplers"]["XXXXL"], "XXXXL " + self.clothing_type)
        self.XXXXXLShirt = shirt(self.XXXXXLSpin.GetValue(), self.base_price, self.settings["production_miltiplers"]["XXXXXL"], "XXXXXL " + self.clothing_type)

        self.order_list = [self.SShirt, self.MShirt, self.LShirt, self.XLShirt, self.XXLShirt, self.XXXLShirt, self.XXXXLShirt, self.XXXXXLShirt] # list of all shirts

        # Do all math and logic
        timestamp = datetime.datetime.today()
        if self.user_id not in return_user_ids():
            custom_functions.yaml_loader(self.userdata_location + str(self.user_id) + ".yaml", {'customer': {'previous_orders': {str(timestamp.month) + "-" + str(timestamp.day) + "-" + str(timestamp.year): {'cost': 30, 'other': 'yote'}}}})

        # Export everything
        if self.export_format == "pdf":
            None
        elif self.export_format == "txt":
            for size in self.order_list:
                if size.get_cost() > 0:
                    print(size.get_invoice_text())
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
