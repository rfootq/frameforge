import os, glob
import json

from PySide import QtCore, QtGui

import FreeCADGui as Gui
import FreeCAD as App

from freecad.frameforge.translate_utils import translate
from freecad.frameforge import PROFILESPATH, PROFILEIMAGES_PATH, ICONPATH, UIPATH

from freecad.frameforge.profile import Profile

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


        param = App.ParamGet("User parameter:BaseApp/Preferences/Frameforge")
        default_material_index = self.form.combo_material.findText(param.GetString("Default Profile Material"))
        if default_material_index > -1:
            self.form.combo_material.setCurrentIndex(default_material_index)

            default_family_index = self.form.combo_family.findText(param.GetString("Default Profile Family"))
            if default_family_index > -1:
                self.form.combo_family.setCurrentIndex(default_family_index)

                default_size_index = self.form.combo_size.findText(param.GetString("Default Profile Size"))
                if default_size_index > -1:
                    self.form.combo_size.setCurrentIndex(default_size_index)


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

        self.form.label_norm.setText(self.profiles[material][family]['norm'])
        self.form.label_unit.setText(self.profiles[material][family]['unit'])

        self.form.combo_size.clear()
        self.form.combo_size.addItems([s for s in self.profiles[material][family]['sizes']])
        

    def on_size_changed(self, index):
        material = str(self.form.combo_material.currentText())
        family = str(self.form.combo_family.currentText())
        size = str(self.form.combo_size.currentText())

        if size != '':
            profile  = self.profiles[material][family]['sizes'][size]

            SETTING_MAP = {
                "Height": self.form.sb_height,
                "Width": self.form.sb_width,
                "Thickness": self.form.sb_main_thickness,
                "Flange Thickness": self.form.sb_flange_thickness,
                "Radius1": self.form.sb_radius1,
                "Radius2": self.form.sb_radius2,
                "Weight": self.form.sb_weight
            }

            self.form.sb_height.setEnabled(False)
            self.form.sb_width.setEnabled(False)
            self.form.sb_main_thickness.setEnabled(False)
            self.form.sb_flange_thickness.setEnabled(False)
            self.form.sb_radius1.setEnabled(False)
            self.form.sb_radius2.setEnabled(False)
            self.form.sb_weight.setEnabled(False)

            for s in profile:
                if s == "Size":
                    continue

                if s not in SETTING_MAP:
                    raise ValueError('Setting Unkown')

                sb = SETTING_MAP[s]
                sb.setEnabled(True)

                sb.setValue(float(profile[s]))



    def on_cb_make_fillet_changed(self, state):
        self.update_image()



    def update_image(self):
        material = str(self.form.combo_material.currentText())
        family = str(self.form.combo_family.currentText())

        img_name = family.replace(' ', "_")
        if self.form.cb_make_fillet.isChecked():
            img_name += "_Fillet"
        img_name += ".png"

        self.form.label_image.setPixmap(QtGui.QPixmap(os.path.join(PROFILEIMAGES_PATH, material, img_name)))


    def open(self):
        App.Console.PrintMessage(translate("frameforge", "Opening CreateProfile\n"))
        self.update_selection()

        App.ActiveDocument.openTransaction("Add Profile")


    def reject(self):
        App.Console.PrintMessage(translate("frameforge", "Rejecting CreateProfile\n"))

        self.clean()
        App.ActiveDocument.abortTransaction()

        return True


    def accept(self):
        App.Console.PrintMessage(translate("frameforge", "Accepting CreateProfile\n"))

        param = App.ParamGet("User parameter:BaseApp/Preferences/Frameforge")
        param.SetString("Default Profile Material", self.form.combo_material.currentText())
        param.SetString("Default Profile Family", self.form.combo_family.currentText())
        param.SetString("Default Profile Size", self.form.combo_size.currentText())

        self.proceed()
        self.clean()

        App.ActiveDocument.commitTransaction()
        App.ActiveDocument.recompute()

        return True

    def clean(self):
        Gui.Selection.removeObserver(self)
        Gui.Selection.removeSelectionGate()


    def proceed(self):
        selection_list = Gui.Selection.getSelectionEx()
        for sketch in selection_list:
            edges = sketch.SubElementNames
            for i, edge in enumerate(edges):
                p_name = "Profile_" + self.form.combo_family.currentText().replace(" ", "_")
                if self.form.cb_size_in_name.isChecked():
                    p_name += "_" + self.form.combo_size.currentText()

                self.make_profile(sketch, edge, p_name)
        

    def make_profile(self, sketch, edge, name):
        # Create an object in current document
        obj = App.ActiveDocument.addObject("Part::FeaturePython", name)
        obj.addExtension("Part::AttachExtensionPython")

        # Create a ViewObject in current GUI
        obj.ViewObject.Proxy = 0
        view_obj = Gui.ActiveDocument.getObject(obj.Name)
        view_obj.DisplayMode = "Flat Lines"


        # Tuple assignment for edge
        feature = sketch.Object
        link_sub = (feature, (edge))
        obj.MapMode = "NormalToEdge"

        try:
            obj.AttachmentSupport = (feature, edge)
        except AttributeError: # for Freecad <= 0.21 support
            obj.Support = (feature, edge)

        if not self.form.cb_reverse_attachment.isChecked():
            #print("Not reverse attachment")
            obj.MapPathParameter = 1
        else:
            #print("Reverse attachment")
            obj.MapPathParameter = 0
            obj.MapReversed = True


        Profile(
            obj,
            self.form.sb_width.value(),
            self.form.sb_height.value(),
            self.form.sb_main_thickness.value(),
            self.form.sb_flange_thickness.value(),
            self.form.sb_radius1.value(),
            self.form.sb_radius2.value(),
            self.form.sb_length.value(),
            self.form.sb_weight.value(),
            self.form.cb_make_fillet.isChecked(), # and self.form.family.currentText() not in ["Flat Sections", "Square", "Round Bar"],
            self.form.cb_height_centered.isChecked(),
            self.form.cb_width_centered.isChecked(),
            self.form.combo_family.currentText(),
            self.form.cb_combined_bevel.isChecked(),
            link_sub
        )



    def addSelection(self, doc, obj, sub, other):
        self.update_selection()

    def clearSelection(self, other):
        self.update_selection()

    def update_selection(self):
        obj_name = ''
        for sel in Gui.Selection.getSelectionEx():
            selected_obj_name = sel.ObjectName
            subs = ''
            for sub in sel.SubElementNames:
                subs += '{},'.format(sub)

            obj_name += selected_obj_name 
            obj_name += " / "
            obj_name += subs
            obj_name += '\n'

        self.form.label_attach.setText(obj_name)




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

        Gui.Selection.addObserver(panel)
        Gui.Selection.addSelectionGate('SELECT Part::Feature SUBELEMENT Edge')

        Gui.Control.showDialog(panel)


    def IsActive(self):
        """Here you can define if the command must be active or not (greyed) if certain conditions
        are met or not. This function is optional."""
        return App.ActiveDocument is not None

Gui.addCommand("FrameForge_CreateProfiles", CreateProfilesCommand())