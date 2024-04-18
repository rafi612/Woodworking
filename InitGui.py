import FreeCAD, FreeCADGui
import os, sys

import fakemodule
path = os.path.dirname(fakemodule.__file__)
translationsPath = os.path.join(path, "translations")
FreeCADGui.addLanguagePath(translationsPath)
FreeCADGui.updateLocale()

class WoodworkingWorkbench (Workbench):
	translate = FreeCAD.Qt.translate

	import fakemodule
	path = os.path.dirname(fakemodule.__file__)
	iconPath = os.path.join(path, "Icons")
	translationsPath = os.path.join(path, "translations")

	MenuText = translate("InitGui", "Woodworking")
	ToolTip = translate("InitGui", "Workbech for woodworking.")
	Icon = os.path.join(iconPath, "Woodworking.png")

	def Initialize(self):
		# uncomment those lines below if you want to add icon from other workbenches
		# however the DraftTools will slow down the FreeCAD loading
		# for woodworking purposes there will be new tools, so do not cry ;-)
		import PartGui, PartDesignGui
		import SketcherGui, SpreadsheetGui
		#import DraftTools

		import loadToolbar
		import loadMenu

		translate = FreeCAD.Qt.translate

		# toolbar
		# ################################################################################################

		self.appendToolbar(translate("Workbench", "Woodworking - default"),
			loadToolbar.getItems("Woodworking - default"))

		self.appendToolbar(translate("Workbench", "Woodworking - copy"),
			loadToolbar.getItems("Woodworking - copy"))

		self.appendToolbar(translate("Workbench", "Woodworking - move"),
			loadToolbar.getItems("Woodworking - move"))

		self.appendToolbar(translate("Workbench", "Woodworking - resize"),
			loadToolbar.getItems("Woodworking - resize"))

		self.appendToolbar(translate("Workbench", "Woodworking - special"),
			loadToolbar.getItems("Woodworking - special"))

		self.appendToolbar(translate("Workbench", "Woodworking - face"),
			loadToolbar.getItems("Woodworking - face"))

		self.appendToolbar(translate("Workbench", "Woodworking - between"),
			loadToolbar.getItems("Woodworking - between"))

		self.appendToolbar(translate("Workbench", "Woodworking - construction"),
			loadToolbar.getItems("Woodworking - construction"))

		self.appendToolbar(translate("Workbench", "Woodworking - dowels and screws"),
			loadToolbar.getItems("Woodworking - dowels and screws"))

		self.appendToolbar(translate("Workbench", "Woodworking - fixture"),
			loadToolbar.getItems("Woodworking - fixture"))

		self.appendToolbar(translate("Workbench", "Woodworking - joinery"),
			loadToolbar.getItems("Woodworking - joinery"))

		self.appendToolbar(translate("Workbench", "Woodworking - drilling holes"),
			loadToolbar.getItems("Woodworking - drilling holes"))

		self.appendToolbar(translate("Workbench", "Woodworking - project manage"),
			loadToolbar.getItems("Woodworking - project manage"))

		self.appendToolbar(translate("Workbench", "Woodworking - code and debug"),
			loadToolbar.getItems("Woodworking - code and debug"))

		self.appendToolbar(translate("Workbench", "Woodworking - dimensions"),
			loadToolbar.getItems("Woodworking - dimensions"))

		self.appendToolbar(translate("Workbench", "Woodworking - router"),
			loadToolbar.getItems("Woodworking - router"))

		self.appendToolbar(translate("Workbench", "Woodworking - decorations"),
			loadToolbar.getItems("Woodworking - decorations"))

		self.appendToolbar(translate("Workbench", "Woodworking - advanced"),
			loadToolbar.getItems("Woodworking - advanced"))

		self.appendToolbar(translate("Workbench", "Woodworking - preview"),
			loadToolbar.getItems("Woodworking - preview"))
		# menu
		# ################################################################################################
		self.appendMenu(translate("MenuItem", "Woo&dworking"), loadMenu.getItems())

	def Activated(self):
		# not needed now, maybe in the future
		return

	def Deactivated(self):
		# not needed now, maybe in the future
		return

	def ContextMenu(self, recipient):
		# not needed now, maybe in the future
		return

	def GetClassName(self):
		return "Gui::PythonWorkbench"

Gui.addWorkbench(WoodworkingWorkbench())
