# Description

FreeCAD is great software and this is extension for Woodworking. The main goal for this workbench is to make furniture designing process at FreeCAD more simple. If you want to make simple furniture for your garage which costs `150 PLN` this workbench is for you.

![intro](https://raw.githubusercontent.com/dprojects/Woodworking/master/Screenshots/intro.gif)

|   |   |
|---|---|
| [![c1r1](https://raw.githubusercontent.com/dprojects/Woodworking/master/Screenshots/matrix/c1r1.png)](https://raw.githubusercontent.com/dprojects/Woodworking/master/Screenshots/matrix/c1r1.png) | [![c2r1](https://raw.githubusercontent.com/dprojects/Woodworking/master/Screenshots/matrix/c2r1.png)](https://raw.githubusercontent.com/dprojects/Woodworking/master/Screenshots/matrix/c2r1.png) |
| [![c1r2](https://raw.githubusercontent.com/dprojects/Woodworking/master/Screenshots/matrix/c1r2.png)](https://raw.githubusercontent.com/dprojects/Woodworking/master/Screenshots/matrix/c1r2.png) | [![c2r2](https://raw.githubusercontent.com/dprojects/Woodworking/master/Screenshots/matrix/c2r2.png)](https://raw.githubusercontent.com/dprojects/Woodworking/master/Screenshots/matrix/c2r2.png) |
| [![c1r3](https://raw.githubusercontent.com/dprojects/Woodworking/master/Screenshots/matrix/c1r3.png)](https://raw.githubusercontent.com/dprojects/Woodworking/master/Screenshots/matrix/c1r3.png) | [![c2r3](https://raw.githubusercontent.com/dprojects/Woodworking/master/Screenshots/matrix/c2r3.png)](https://raw.githubusercontent.com/dprojects/Woodworking/master/Screenshots/matrix/c2r3.png) |
| [![c1r4](https://raw.githubusercontent.com/dprojects/Woodworking/master/Screenshots/matrix/c1r4.png)](https://raw.githubusercontent.com/dprojects/Woodworking/master/Screenshots/matrix/c1r4.png) | [![c2r4](https://raw.githubusercontent.com/dprojects/Woodworking/master/Screenshots/matrix/c2r4.png)](https://raw.githubusercontent.com/dprojects/Woodworking/master/Screenshots/matrix/c2r4.png) |


**For more details see:** 
* YouTube channel dedicated for this workbench at: [YouTube channel](https://www.youtube.com/channel/UCDaABD-__ESAfflopSqZ0ng/videos)
* Woodworking workbench documentation available at: [Docs folder](https://github.com/dprojects/Woodworking/tree/master/Docs)

# Certified platforms

* Stable certified versions download at: [Woodworking/releases](https://github.com/dprojects/Woodworking/releases)
* For cutting edge features download:
	* Woodworking workbench development version from: [the master branch](https://github.com/dprojects/Woodworking/archive/refs/heads/master.zip)
	* FreeCAD version from: [FreeCAD_weekly-builds-30486-2022-09-29-conda-Linux-x86_64-py310.AppImage](https://github.com/FreeCAD/FreeCAD-Bundle/releases/download/weekly-builds/FreeCAD_weekly-builds-30486-2022-09-29-conda-Linux-x86_64-py310.AppImage)

* Current development platform:

		OS: Ubuntu 22.04.1 LTS (XFCE/xubuntu)
		Word size of FreeCAD: 64-bit
		Version: 0.21.30486 (Git) AppImage
		Build type: Release
		Branch: master
		Hash: eb546e25d3f952869e3ec87dca02b58653cb3936
		Python 3.10.6, Qt 5.15.4, Coin 4.0.0, Vtk 9.1.0, OCC 7.6.3
		Locale: English/United States (en_US)
		Installed mods: 
		* Woodworking 0.21.30486

**Note:** To get better stability make sure your current Woodworking workbench version has always the same version number as the FreeCAD version.

# Installation

* Download and unpack `Woodworking` repository.
* Copy the folder `Woodworking` to the FreeCAD module directory (`Mod` folder).

**Note:**

* Xubuntu:
	* FreeCAD version < 0.20.27936: `~.FreeCAD/Mod/Woodworking`
	* FreeCAD version >= 0.20.27936: `~.local/share/FreeCAD/Mod/Woodworking`

# Extras

This woodworking workbench is delivered with several useful extras:

* [Fully parametric examples](https://github.com/dprojects/Woodworking/tree/master/Examples/Parametric) - this folder inside woodworking workbench contains sample furniture projects. All of the furniture examples are parametric. So, you can quickly adopt it to your current project, without designing e.g. bookcase from scratch. You can also add decoration, if needed, or even merge with other projects.
* [Fixture examples](https://github.com/dprojects/Woodworking/tree/master/Examples/Fixture) - this is new approach to 3D modeling. For example you can replace any Cylinder with realistic looking detailed screw. This is very powerful feature and gives a lot of flexibility and simplifies the process of making model detailed.
* [Texture samples](https://commons.wikimedia.org/w/index.php?title=Special:ListFiles/Dprojects&ilshowall=1) - sample textures for woodworking projects purposes.

# Translations

For Woodworking workbench translation see dedicated directory: [translations](https://github.com/dprojects/Woodworking/tree/master/translations)

# API for developers

The Woodworking workbench has also API for developers. You can also create your own tools and extend the workbench: 
* MagicPanels library available at: [MagicPanels.py](https://raw.githubusercontent.com/dprojects/Woodworking/master/Tools/MagicPanels/MagicPanels.py)
* API documentation: [MagicPanelsAPI.md](https://github.com/dprojects/Woodworking/blob/master/Docs/MagicPanelsAPI.md)
* You can also browse MagicPanels library directly from Woodworking workbench via: [scanObjects tool](https://github.com/dprojects/Woodworking/tree/master/Docs#scanobjects)

# Contact

* If you have any questions, comments, feature requests, proposition for improvements, please open issue at: [issue tracker](https://github.com/dprojects/Woodworking/issues)
* Also we can discuss: [FreeCAD forum thread](https://forum.freecadweb.org/viewtopic.php?f=3&t=8247).

# License

MIT for all Woodworking workbench content.
