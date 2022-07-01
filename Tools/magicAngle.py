import FreeCAD, FreeCADGui 
import Draft
from PySide import QtGui, QtCore


# ############################################################################
# Qt Main
# ############################################################################


def showQtGUI():
	
	class QtMainClass(QtGui.QDialog):
		
		# ############################################################################
		# globals
		# ############################################################################

		gObj = ""
		gSphere = ""
		gCenter = []
		gCenterIndex = 0
		gStep = 15
		gNoSelection = "select panel to rotate"
		
		# ############################################################################
		# init
		# ############################################################################

		def __init__(self):
			super(QtMainClass, self).__init__()
			self.initUI()

		def initUI(self):

			# ############################################################################
			# set screen
			# ############################################################################
			
			# tool screen size
			toolSW = 220
			toolSH = 270
			
			# active screen size (FreeCAD main window)
			gSW = FreeCADGui.getMainWindow().width()
			gSH = FreeCADGui.getMainWindow().height()

			# tool screen position
			gPW = int( gSW - toolSW )
			gPH = int( gSH - toolSH )

			# ############################################################################
			# main window
			# ############################################################################
			
			self.result = userCancelled
			self.setGeometry(gPW, gPH, toolSW, toolSH)
			self.setWindowTitle("magicAngle")
			self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

			# ############################################################################
			# options - selection mode
			# ############################################################################
			
			# screen
			info = ""
			info += "                                             "
			info += "                                             "
			info += "                                             "
			self.s1S = QtGui.QLabel(info, self)
			self.s1S.move(10, 10)

			# button
			self.s1B1 = QtGui.QPushButton("refresh selection", self)
			self.s1B1.clicked.connect(self.getSelected)
			self.s1B1.setFixedWidth(200)
			self.s1B1.move(10, 40)

			# ############################################################################
			# options - rotation center point
			# ############################################################################

			# label
			self.o0L = QtGui.QLabel("Rotation point:", self)
			self.o0L.move(10, 83)

			# button
			self.o0B1 = QtGui.QPushButton("<", self)
			self.o0B1.clicked.connect(self.setCenterP)
			self.o0B1.setFixedWidth(50)
			self.o0B1.move(105, 80)
			self.o0B1.setAutoRepeat(True)
			
			# button
			self.o0B2 = QtGui.QPushButton(">", self)
			self.o0B2.clicked.connect(self.setCenterN)
			self.o0B2.setFixedWidth(50)
			self.o0B2.move(160, 80)
			self.o0B2.setAutoRepeat(True)

			# ############################################################################
			# options - X axis
			# ############################################################################

			# label
			self.o1L = QtGui.QLabel("X axis (yaw):", self)
			self.o1L.move(10, 123)

			# button
			self.o1B1 = QtGui.QPushButton("<", self)
			self.o1B1.clicked.connect(self.setX1)
			self.o1B1.setFixedWidth(50)
			self.o1B1.move(105, 120)
			self.o1B1.setAutoRepeat(True)
			
			# button
			self.o1B2 = QtGui.QPushButton(">", self)
			self.o1B2.clicked.connect(self.setX2)
			self.o1B2.setFixedWidth(50)
			self.o1B2.move(160, 120)
			self.o1B2.setAutoRepeat(True)
			
			# ############################################################################
			# options - Y axis
			# ############################################################################

			# label
			self.o2L = QtGui.QLabel("Y axis (pitch):", self)
			self.o2L.move(10, 153)

			# button
			self.o2B1 = QtGui.QPushButton("<", self)
			self.o2B1.clicked.connect(self.setY1)
			self.o2B1.setFixedWidth(50)
			self.o2B1.move(105, 150)
			self.o2B1.setAutoRepeat(True)
			
			# button
			self.o2B2 = QtGui.QPushButton(">", self)
			self.o2B2.clicked.connect(self.setY2)
			self.o2B2.setFixedWidth(50)
			self.o2B2.move(160, 150)
			self.o2B2.setAutoRepeat(True)

			# ############################################################################
			# options - Z axis
			# ############################################################################

			# label
			self.o3L = QtGui.QLabel("Z axis (roll):", self)
			self.o3L.move(10, 183)

			# button
			self.o3B1 = QtGui.QPushButton("<", self)
			self.o3B1.clicked.connect(self.setZ1)
			self.o3B1.setFixedWidth(50)
			self.o3B1.move(105, 180)
			self.o3B1.setAutoRepeat(True)
			
			# button
			self.o3B2 = QtGui.QPushButton(">", self)
			self.o3B2.clicked.connect(self.setZ2)
			self.o3B2.setFixedWidth(50)
			self.o3B2.move(160, 180)
			self.o3B2.setAutoRepeat(True)
			
			# ############################################################################
			# options - additional
			# ############################################################################

			# label
			self.o4L = QtGui.QLabel("Angle step:", self)
			self.o4L.move(10, 213)

			# text input
			self.o4E = QtGui.QLineEdit(self)
			self.o4E.setText(str(self.gStep))
			self.o4E.setFixedWidth(50)
			self.o4E.move(105, 210)
			
			# ############################################################################
			# show & init defaults
			# ############################################################################

			# show window
			self.show()

			# init
			self.getSelected()

		# ############################################################################
		# actions - internal functions
		# ############################################################################

		# ############################################################################
		def setCenterPoints(self):
			
			self.gCenter = []
			
			try:
			
				# you can add new center points here, if needed
				
				v = self.gObj.Shape.Faces[4].Vertexes[0]
				self.gCenter.append(FreeCAD.Vector(float(v.X), float(v.Y), float(v.Z)))
			
				v = self.gObj.Shape.Faces[4].Vertexes[1]
				self.gCenter.append(FreeCAD.Vector(float(v.X), float(v.Y), float(v.Z)))

				v = self.gObj.Shape.Faces[4].Vertexes[2]
				self.gCenter.append(FreeCAD.Vector(float(v.X), float(v.Y), float(v.Z)))

				v = self.gObj.Shape.Faces[4].Vertexes[3]
				self.gCenter.append(FreeCAD.Vector(float(v.X), float(v.Y), float(v.Z)))

				v = self.gObj.Shape.Faces[5].Vertexes[0]
				self.gCenter.append(FreeCAD.Vector(float(v.X), float(v.Y), float(v.Z)))

				v = self.gObj.Shape.Faces[5].Vertexes[1]
				self.gCenter.append(FreeCAD.Vector(float(v.X), float(v.Y), float(v.Z)))

				v = self.gObj.Shape.Faces[5].Vertexes[2]
				self.gCenter.append(FreeCAD.Vector(float(v.X), float(v.Y), float(v.Z)))

				v = self.gObj.Shape.Faces[5].Vertexes[3]
				self.gCenter.append(FreeCAD.Vector(float(v.X), float(v.Y), float(v.Z)))
		
			except:
				self.gCenter.append(FreeCAD.Vector(float(0.0), float(0.0), float(0.0)))
			
		def setCenterSphere(self):
			
			v = self.gCenter[self.gCenterIndex]
			self.gSphere.Placement = FreeCAD.Placement(v, FreeCAD.Rotation(0, 0, 0))
			self.gSphere.ViewObject.ShapeColor = (0.0, 0.0, 0.0, 0.0)
			self.gSphere.ViewObject.Transparency = 83
			
			# could be panel thickness, but some more complicated objects 
			# supported by Draft.rotate may not have thickness available so well
			# better leave it to not suppress Draft.rotate functionality
			self.gSphere.Radius = 20
			
			FreeCAD.activeDocument().recompute()

		def setRotation(self, iAxis, iAngle):
			
			Draft.rotate(self.gObj, iAngle, self.gCenter[self.gCenterIndex], iAxis, False)
			FreeCADGui.Selection.clearSelection()
			FreeCAD.activeDocument().recompute()

			self.setCenterPoints()
			self.setCenterSphere()

		# ############################################################################
		# actions - functions for actions
		# ############################################################################

		# ############################################################################
		def getSelected(self):

			try:

				try:
					FreeCAD.activeDocument().removeObject(str(self.gSphere.Name))
				except:
					skip = 1

				self.gObj = FreeCADGui.Selection.getSelection()[0]
				self.s1S.setText(str(self.gObj.Label))
				FreeCADGui.Selection.clearSelection()
				
				self.gSphere = FreeCAD.ActiveDocument.addObject("Part::Sphere","magicAnglePoint")
				self.setCenterPoints()
				self.setCenterSphere()

			except:

				self.s1S.setText(self.gNoSelection)
				return -1
			
		# ############################################################################
		def setCenterP(self):
			
			try:
				if self.gCenterIndex - 1 < 0:
					self.gCenterIndex = len(self.gCenter) - 1
				else:
					self.gCenterIndex = self.gCenterIndex - 1
					
				self.setCenterSphere()
			except:
				self.s1S.setText(self.gNoSelection)
			
		def setCenterN(self):
			
			try:
				if self.gCenterIndex + 1 > len(self.gCenter) - 1:
					self.gCenterIndex = 0
				else:
					self.gCenterIndex = self.gCenterIndex + 1
					
				self.setCenterSphere()
			except:
				self.s1S.setText(self.gNoSelection)
				
		# ############################################################################
		def setX1(self):
			
			try:
				self.gStep = int(self.o4E.text())
				self.setRotation(FreeCAD.Vector(1, 0, 0), self.gStep)
			except:
				self.s1S.setText(self.gNoSelection)
			
		def setX2(self):
			
			try:
				self.gStep = int(self.o4E.text())
				self.setRotation(FreeCAD.Vector(1, 0, 0), -self.gStep)
			except:
				self.s1S.setText(self.gNoSelection)
			
		def setY1(self):
			
			try:
				self.gStep = int(self.o4E.text())
				self.setRotation(FreeCAD.Vector(0, 1, 0), self.gStep)
			except:
				self.s1S.setText(self.gNoSelection)
		
		def setY2(self):
			
			try:
				self.gStep = int(self.o4E.text())
				self.setRotation(FreeCAD.Vector(0, 1, 0), -self.gStep)
			except:
				self.s1S.setText(self.gNoSelection)

		def setZ1(self):
			
			try:
				self.gStep = int(self.o4E.text())
				self.setRotation(FreeCAD.Vector(0, 0, 1), self.gStep)
			except:
				self.s1S.setText(self.gNoSelection)
		
		def setZ2(self):
			
			try:
				self.gStep = int(self.o4E.text())
				self.setRotation(FreeCAD.Vector(0, 0, 1), -self.gStep)
			except:
				self.s1S.setText(self.gNoSelection)

	# ############################################################################
	# final settings
	# ############################################################################

	userCancelled = "Cancelled"
	userOK = "OK"
	
	form = QtMainClass()
	form.exec_()
	
	if form.result == userCancelled:
		if form.gSphere != "":
			try:
				FreeCAD.activeDocument().removeObject(str(form.gSphere.Name))
			except:
				skip = 1
		pass

# ###################################################################################################################
# MAIN
# ###################################################################################################################


showQtGUI()


# ###################################################################################################################
