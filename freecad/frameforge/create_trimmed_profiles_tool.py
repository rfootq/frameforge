import os, glob
import json

from PySide import QtCore, QtGui

import FreeCADGui as Gui
import FreeCAD as App

import Part, ArchCommands
import BOPTools.SplitAPI

from freecad.frameforge.translate_utils import translate
from freecad.frameforge import PROFILESPATH, PROFILEIMAGES_PATH, ICONPATH, UIPATH



class CreateTrimmedProfileTaskPanel():
    def __init__(self):
        ui_file = os.path.join(UIPATH, "create_trimmed_profiles.ui")
        self.form = Gui.PySideUic.loadUi(ui_file)

        self.initialize_ui()

    def initialize_ui(self):
        add_icon = QtGui.QIcon(os.path.join(ICONPATH, "list-add.svg"))
        remove_icon = QtGui.QIcon(os.path.join(ICONPATH, "list-remove.svg"))
        coped_type_icon = QtGui.QIcon(os.path.join(ICONPATH, "corner-coped-type.svg"))
        simple_type_icon = QtGui.QIcon(os.path.join(ICONPATH, "corner-simple-type.svg"))
        
        QSize = QtCore.QSize(32, 32)

        self.form.rb_copedcut.setIcon(coped_type_icon)
        self.form.rb_copedcut.setIconSize(QSize)

        self.form.rb_simplecut.setIcon(simple_type_icon)
        self.form.rb_simplecut.setIconSize(QSize)

        self.form.add_trimmed_object_button.setIcon(add_icon)
        self.form.add_boundary_button.setIcon(add_icon)
        self.form.remove_boundary_button.setIcon(remove_icon)



class TrimProfileCommand():
    def GetResources(self):
        return {
            "Pixmap": os.path.join(ICONPATH, "corner-end-trim.svg"),
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
        panel = CreateTrimmedProfileTaskPanel()

        Gui.Control.showDialog(panel)


Gui.addCommand("FrameForge_TrimProfiles", TrimProfileCommand())
