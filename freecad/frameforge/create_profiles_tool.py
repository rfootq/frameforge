import os

from PySide import QtCore, QtGui

import FreeCADGui as Gui
import FreeCAD as App

from freecad.frameforge.translate_utils import translate
from freecad.frameforge import WAREHOUSEPATH, ICONPATH, UIPATH

class CreateProfileTaskPanel():
    def __init__(self):
        ui_file = os.path.join(UIPATH, "create_profiles.ui")
        self.form = Gui.PySideUic.loadUi(ui_file)

        self.initialize_ui()

    def initialize_ui(self):
        self.form.label_image.setPixmap(QtGui.QPixmap(os.path.join(WAREHOUSEPATH, "Warehouse.png")))


    def open(self):
        App.Console.PrintMessage(translate("frameforge", "Opening CreateProfile\n"))

        App.ActiveDocument.openTransaction("Add Profile")


    def reject(self):
        App.Console.PrintMessage(translate("frameforge", "Rejecting CreateProfile\n"))

        App.ActiveDocument.abortTransaction()

        return True


    def accept(self):
        App.Console.PrintMessage(translate("frameforge", "Accepting CreateProfile\n"))

        self.proceed()

        App.ActiveDocument.commitTransaction()
        App.ActiveDocument.recompute()

        return True


    def proceed(self):
        doc = App.ActiveDocument

        box = doc.addObject("Part::Box", "myBox")

        box.Height = 50
        box.Width = 60
        box.Length = 30



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
        return App.ActiveDocument is not None

Gui.addCommand("FrameForge_CreateProfiles", CreateProfilesCommand())