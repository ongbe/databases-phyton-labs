"""
    Program-starting module. Creates controller object and starts it's work
"""

from gui.CSVTableController import CSVTableController

controller = CSVTableController()
controller.start("login.txt")
