import os
import FreeCADGui as Gui
import FreeCAD as App

from freecad.frameforge.translate_utils import translate
from freecad.frameforge import ICONPATH, UIPATH

class CreateProfileTaskPanel():
    def __init__(self):
        ui_file = os.path.join(UIPATH, "create_profiles.ui")
        self.form = Gui.PySideUic.loadUi(ui_file)



    def open(self):
        App.Console.PrintMessage(translate(
            "frameforge",
            "Opening CreateProfile") + "\n")

    def accept(self):
        App.Console.PrintMessage(translate(
            "frameforge",
            "Accepting CreateProfile") + "\n")



class CreateProfilesCommand():
    """Create Profiles with standards dimensions"""

    def GetResources(self):
        return {"Pixmap"  : os.path.join(ICONPATH, "warehouse_profiles.svg"),
                "Accel"   : "Shift+S", # a default shortcut (optional)
                "MenuText": "Create Profile",
                "ToolTip" : "Create new profiles from Edges"}

    def Activated(self):
        """Do something here"""

        panel = CreateProfileTaskPanel()
        Gui.Control.showDialog(panel)

    def IsActive(self):
        """Here you can define if the command must be active or not (greyed) if certain conditions
        are met or not. This function is optional."""
        return True

Gui.addCommand("FrameForge_CreateProfiles", CreateProfilesCommand())