import os
import FreeCADGui as Gui
import FreeCAD as App
from freecad.frameforge.translate_utils import translate

from freecad.frameforge import ICONPATH, TRANSLATIONSPATH


class FrameForge(Gui.Workbench):
    """
    class which gets initiated at startup of the gui
    """
    MenuText = translate("frameforge", "FrameForge")
    ToolTip = translate("frameforge", "a simple FrameForge")
    Icon = os.path.join(ICONPATH, "metalwb.svg")
    toolbox = ["FrameForge_CreateProfiles"]

    def GetClassName(self):
        return "Gui::PythonWorkbench"

    def Initialize(self):
        """
        This function is called at the first activation of the workbench.
        here is the place to import all the commands
        """
        from freecad.frameforge import create_profiles_tool

        # Add translations path
        Gui.addLanguagePath(TRANSLATIONSPATH)
        Gui.updateLocale()

        App.Console.PrintMessage(translate(
            "frameforge",
            "Switching to frameforge") + "\n")

        self.appendToolbar(translate("Toolbar", "Tools"), self.toolbox)
        self.appendMenu(translate("Menu", "Tools"), self.toolbox)

    def Activated(self):
        '''
        code which should be computed when a user switch to this workbench
        '''
        App.Console.PrintMessage(translate(
            "frameforge",
            "Workbench frameforge activated.") + "\n")

    def Deactivated(self):
        '''
        code which should be computed when this workbench is deactivated
        '''
        App.Console.PrintMessage(translate(
            "frameforge",
            "Workbench frameforge de-activated.") + "\n")


Gui.addWorkbench(FrameForge())
