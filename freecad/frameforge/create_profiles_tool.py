import os, glob
import json

from PySide import QtCore, QtGui

import FreeCADGui as Gui
import FreeCAD as App

from freecad.frameforge.translate_utils import translate
from freecad.frameforge import PROFILESPATH, PROFILEIMAGES_PATH, ICONPATH, UIPATH

class CreateProfileTaskPanel():
    def __init__(self):
        ui_file = os.path.join(UIPATH, "create_profiles.ui")
        self.form = Gui.PySideUic.loadUi(ui_file)

        self.load_data()
        self.initialize_ui()


    def load_data(self):
        self.profiles = {}

        files = [f for f in os.listdir(PROFILESPATH) if f.endswith('.json')]

        for f in files:
            material_name = os.path.splitext(f)[0].capitalize()

            with open(os.path.join(PROFILESPATH, f)) as fd:
                self.profiles[material_name] = json.load(fd)


    def initialize_ui(self):
        self.form.label_image.setPixmap(QtGui.QPixmap(os.path.join(PROFILEIMAGES_PATH, "Warehouse.png")))

        self.form.combo_material.currentIndexChanged.connect(self.on_material_changed)
        self.form.combo_family.currentIndexChanged.connect(self.on_family_changed)
        self.form.combo_size.currentIndexChanged.connect(self.on_size_changed)

        self.form.cb_make_fillet.stateChanged.connect(self.on_cb_make_fillet_changed)


        self.form.combo_material.addItems([k for k in self.profiles])


    def on_material_changed(self, index):
        material = str(self.form.combo_material.currentText())

        self.form.combo_family.clear()
        self.form.combo_family.addItems([f for f in self.profiles[material]])

    def on_family_changed(self, index):
        material = str(self.form.combo_material.currentText())
        family = str(self.form.combo_family.currentText())

        self.form.cb_make_fillet.setChecked(self.profiles[material][family]['fillet'])
        self.form.cb_make_fillet.setEnabled(self.profiles[material][family]['fillet'])

        self.update_image()
        

    def on_size_changed(self, index):
        pass


    def on_cb_make_fillet_changed(self, state):
        self.update_image()



    def update_image(self):
        family = str(self.form.combo_family.currentText())

        img_name = family.replace(' ', "_")
        if self.form.cb_make_fillet.isChecked():
            img_name += "_Fillet"
        img_name += ".png"
        App.Console.PrintMessage(translate("frameforge", img_name + "\n"))
        self.form.label_image.setPixmap(QtGui.QPixmap(os.path.join(PROFILEIMAGES_PATH, img_name)))


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