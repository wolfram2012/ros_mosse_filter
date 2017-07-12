OPTIMIZED CORRELATION OUTPUT FILTERS TOOLSET (OCOF)
    by David S. Bolme

This distribution contains reference source code for creating and using MOSSE and ASEF correlation filters and also performing fast visual tracking.  This distribution is intended only for research and evaluation purposes.  Commercial use may require additional licenses from Colorado State University (http://www.csuventures.org).  See the the license for more details.

The source code presented here implements techniques described in:

OPTIMIZED CORRELATION FILTERS FOR SIGNAL PROCESSING
DS Bolme, JR Beveridge, BA Draper
US Patent App. 12/797,241

Theory and applications of optimized correlation output filters
DS Bolme, Ph.D. Dissertation
COLORADO STATE UNIVERSITY

Average of synthetic exact filters
DS Bolme, BA Draper, JR Beveridge
Computer Vision and Pattern Recognition, 2009. CVPR 2009.

Visual object tracking using adaptive correlation filters
DS Bolme, JR Beveridge, BA Draper, YM Lui
Computer Vision and Pattern Recognition (CVPR), 2010

Simple real-time human detection using a single correlation filter
DS Bolme, YM Lui, BA Draper, JR Beveridge
Performance Evaluation of Tracking and Surveillance (PETS-Winter), 2009

=============================
INSTALLATION WITH VIRTUAL BOX
=============================
The easiest way to run the correlation filter software is to use virtual box which can run a virtual machine from that is downloaded from the CSU website.  To accomplish this do the following:

 1. Download Virtual Box from https://www.virtualbox.org (Version 4.1.18 or later)
 2. Download the OCOF Toolkit Virtual Machine from http://www.cs.colostate.edu/~vision/ocof.html
 3. Unzip the downloaded file.
 4. Double click the "OCOF Ubuntu.vbox" file to start the virtual machine. 

The OCOF python source code is preinstalled and ready to run in Eclipse or through the command line.  The location is "/home/pyvision/workspace/OCOFToolkit".  Within the toolkit there are two "example" files that can be run which test the tracker or correlation filter training and testing.  

From eclipse you can right click the files in the examples directory and select "Run As -> Python Run" to start the scripts.

From the command line you can change directories into the examples directory and then run the files with python.
 > cd /home/pyvision/workspace/OCOFToolkit/examples
 > python basic_tracking.py
 > python filter_training.py

After the commands are executed the resulting images should be shown.  The images will be stored in the "/tmp" directory and will automatically be deleted when the virtual machine is rebooted.  It should be relatively easy to modify those files to use your own data or videos.

=========================================
INSTALLATION ON WINDOWS, MACOS, AND LINUX
========================================= 

It is possible to install and run the OCOF Toolset on most platforms although it may require some experience with Python programming.  The OCOF toolkit uses the PyVision library for most image processing function. Additional documentation can be found at the pyvision website: pyvision.sf.net

=========================
INSTALLATION DEPENDENCIES
=========================

The algorithms should work with Python 2.6 or later and require a few open source Python modules.  Below are the dependencies required for the toolset with the versions with which the algorithm was tested:
 * Python 2.6.1
 * Numpy/Scipy
 * OpenCV 2.2
 * PIL 1.1.7
 * PyVision (Included with the distribution

==================
MACOS INSTALLATION
==================

As of the most current release we recommend using MacPorts for installation on MacOS, which will keep the dependencies up-to-date.  To get MacPorts follow the instructions here: 

http://www.macports.org/install.php 

The instructions here follow:

http://sourceforge.net/apps/mediawiki/pyvision/index.php?title=Installation_MacOS_X_Snow_Leopard#Installing_with_Python2.6_.2F_MacPorts_.2F_64bit

First install Python 2.7
$ sudo port install python27

To set the new python as the default run the command...

$ sudo port install python_select
$ sudo python_select python27

Install PIL, NumPy, and Scipy. (These depend on the numerical library ATLAS which may take many hours to compile.)

$ sudo port install py27-pil py27-numpy py27-scipy

Install OpenCV with python bindings.

$ sudo port install opencv +python27

Download and unzip OCOF Toolset

Update the PYTHONPATH environment variable to point at the src directory.

$ export PYTHONPATH=<PATH_TO_TOOLSET>/OCOFToolset/src/

====================
WINDOWS INSTALLATION
====================

For windows the python components needed to run the toolset will be installed using binary packages.  The following steps describe the packages that need to be installed and the order in which to install them.  

Install Python 2.7 (to C:\Python27): 
http://python.org/ftp/python/2.7.2/python-2.7.2.msi

Download and install OpenCV from this URL:
http://sourceforge.net/projects/opencvlibrary/files/opencv-win/2.3.1/OpenCV-2.3.1-win-superpack.exe/download
Move the directory to C:\OpenCV

Copy c:\OpenCV\build\python\27\cv.* to c:\Python27\lib\site-packages

Install NumPy from this URL:
http://sourceforge.net/projects/numpy/files/NumPy/1.6.1/numpy-1.6.1-win32-superpack-python2.7.exe/download

Install SciPy from this URL:
http://sourceforge.net/projects/scipy/files/scipy/0.9.0/scipy-0.9.0-win32-superpack-python2.7.exe/download

Install Python Imaging Library from this URL (This version has a correction for a font loading problem found in pythonware distribution):
http://www.lfd.uci.edu/~gohlke/pythonlibs/ayroe8qu/PIL-1.1.7.win32-py2.7.exe

Download and unzip OCOF Toolset

The following paths need to be set up in your environment variables.  After adding the variables make sure to close any command prompt windows so that any new command windows get the new variables.
Add C:\Python27 to path
Add C:\openCV\build\x86\vc10\bin to path (for the DLL files)
Create a new environment variable PYTHONPATH=C:\OCOFToolset\src

Run python from command line and try these commands to make sure all the libraries can be loaded.
   import numpy
   import scipy
   import PIL
   import cv
   import pyvision

These should all run without error.  No output is expected.

You should now be able to run the executable scripts in the bin directory using the command python bin/script_name.py

=============
WINDOWS NOTES
=============

Windows does not come with the bash scripting language that some of the testing scripts  require.  This should be available through cygwin.  Many path names are in unix format so they may need to be updated to run this software on windows.

There is apparently a Font missing with the Python Imaging Library distribution from pythonware that will cause the import of pyvision.Plot to fail.  This can be fixed by using an alternate PIL,  the PIL-1.1.7.win32-py2.7.exe from http://www.lfd.uci.edu/~gohlke/pythonlibs/.

==================
LINUX INSTALLATION
================== 

Due to the differences in linux vendors and how software packages are installed, linux is not supported.  All of the software is available for linux and the CSU evaluation systems has been run on both Ubuntu and Fedora.  Binary installers for dependencies like opencv, PIL, Numpy and Scipy are are available on most linux distributions.  We would suggest using the MacOS installation instructions as a guide for getting things up and running on linux although the process will vary on different linux distributions.


