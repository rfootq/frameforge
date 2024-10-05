import os
import FreeCADGui as Gui
import FreeCAD as App
from freecad.frameforge.translate_utils import translate
from freecad. frameforge import my_numpy_function

ICONPATH = os.path.join(os.path.dirname(__file__), "resources")
TRANSLATIONSPATH = os.path.join(os.path.dirname(__file__), "resources/translations")

class FrameForge(Gui.Workbench):
    """
    class which gets initiated at startup of the gui
    """
    MenuText = translate("frameforge", "FrameForge")
    ToolTip = translate("frameforge", "a simple FrameForge")
    Icon = os.path.join(ICONPATH, "frameforge.svg")
    toolbox = []

    def GetClassName(self):
        return "Gui::PythonWorkbench"

    def Initialize(self):
        """
        This function is called at the first activation of the workbench.
        here is the place to import all the commands
        """
        # Add translations path
        Gui.addLanguagePath(TRANSLATIONSPATH)
        Gui.updateLocale()

        App.Console.PrintMessage(translate(
            "frameforge",
            "Switching to frameforge") + "\n")
        App.Console.PrintMessage(translate(
            "frameforge",
            "Run a numpy function:") + "sqrt(100) = {}\n".format(my_numpy_function.my_foo(100)))

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
