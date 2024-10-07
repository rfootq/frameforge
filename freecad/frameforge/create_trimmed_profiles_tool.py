import os, glob
import json

from PySide import QtCore, QtGui

import FreeCADGui as Gui
import FreeCAD as App

import Part, ArchCommands
import BOPTools.SplitAPI

from freecad.frameforge.translate_utils import translate
from freecad.frameforge import PROFILESPATH, PROFILEIMAGES_PATH, ICONPATH, UIPATH



class TrimmedProfileTaskPanel():
    def __init__(self):
        ui_file = os.path.join(UIPATH, "create_trimmed_profiles.ui")
        self.form = Gui.PySideUic.loadUi(ui_file)

        # self.initialize_ui()



class TrimProfileCommand():
    def GetResources(self):
        return {
            "Pixmap": os.path.join(ICONPATH, "corner.svg"),
            "MenuText": translate("MetalWB", "Trim Profile"),
            "Accel": "M, C",
            "ToolTip": translate("MetalWB", "<html><head/><body><p><b>Trim a profile</b> \
                    <br><br> \
                    Select a profile then another profile's faces. \
                    </p></body></html>"),
        }

    def IsActive(self):
        if App.ActiveDocument:
            if len(Gui.Selection.getSelection()) > 0:
                active = False
                for sel in Gui.Selection.getSelection():
                    if hasattr(sel, 'Target'):
                        active = True
                    elif hasattr(sel, 'TrimmedBody'):
                        active = True
                    else:
                        return False
                return active
            else:
                return True
        return False

    def Activated(self):
        panel = TrimmedProfileTaskPanel()

        Gui.Control.showDialog(panel)


Gui.addCommand("FrameForge_TrimProfiles", TrimProfileCommand())
