import os
import FreeCADGui as Gui
import FreeCAD as App

from freecad.frameforge import ICONPATH


class CreateProfilesClass():
    """Create Profiles with standards dimensions"""

    def GetResources(self):
        return {"Pixmap"  : os.path.join(ICONPATH, "warehouse_profiles.svg"),
                "Accel"   : "Shift+S", # a default shortcut (optional)
                "MenuText": "Create Profile",
                "ToolTip" : "Create new profiles from Edges"}

    def Activated(self):
        """Do something here"""
        return

    def IsActive(self):
        """Here you can define if the command must be active or not (greyed) if certain conditions
        are met or not. This function is optional."""
        return True

Gui.addCommand("CreateProfiles", CreateProfilesClass())