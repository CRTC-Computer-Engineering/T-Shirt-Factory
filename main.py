#!/usr/bin/env python

import wx
import logging as log # Import logging library as log in the code
import gui.noname as gui # Import our custom gui as gui


# Function by Nathan
def return_dollar(dollar_value):
    return "$" + str(dollar_value) # Concanate strings

class tshirt_factory(gui.root_frame): # Class for our app frame
    def __init__(self, parent): # Runs once when we init
        gui.root_frame.__init__(self, parent) # Sets root_frame in gui to the init of gui

        self.UserIdComboBox.SetValue(["Yeeet", "yote"])
        log.debug(self.UserIdComboBox.GetCurrentSelection())

    # Function by joe
    def export_all(self, event): # Exports everything at once
        log.info("Ran export all.") # Debug message
        return None

if __name__ == "__main__":
    log.basicConfig(level=log.DEBUG) # Set logging level
    log.debug("Program Started.") # Debug message

    app = wx.App(redirect=False) # Show console output for errors
    root_window = tshirt_factory(None) # No parent
    root_window.Show() # Show the window
    app.MainLoop() # Run the main GUI loop
