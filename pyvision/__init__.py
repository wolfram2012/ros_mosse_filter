# PyVision License
#
# Copyright (c) 2006-2011 David S. Bolme
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 
# 1. Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
# 
# 2. Redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution.
# 
# 3. Neither name of copyright holders nor the names of its contributors
# may be used to endorse or promote products derived from this software
# without specific prior written permission.
# 
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# ``AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE REGENTS OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

'''
The top level of this package contains some basic types used throughout 
PyVision.  Subpackages some of the more advanced functionality of the 
PyVision library.  These include:

    * Image Processing    
    * Detection           
    * Machine Learning    
    * Optimization/Search 
    * Face Recognition    
    * Analysis            

Typically, all these types are used in a program.  A good convention is to 
import the pyvision library as "pv" and then prefix all function names with "pv." 
This will avoid possible namespace conflicts. For example::

    import pyvision as pv
    im = pv.Image(filename) 
    im.annotateLabel(pv.Point(10,10),"Hello, World!")
    im.show()
'''

'''
-----------------------------------------------------------------------------
                            ALGORITHM DIRECTORY
Algorithm Name        Problem             Module
-----------------------------------------------------------------------------
Support Vector Mach.  classify/regression pyvision.vector.SVM
PCA

Cascade Classifier    face/object detect  pyvision.face.CascadeClassifier
PCA (Face)            face recognition    pyvision.face.PCA

Genetic Algorithm     optimization        pyvision.optimize.GeneticAlgorithm
'''

import unittest
import sys

__version__ = "0.9.0 $Rev: 406 $"
__info__ = "$Id: __init__.py 406 2012-01-05 17:27:43Z svohara $"
__license__= '''
PyVision License

Copyright (c) 2006-2010 David S. Bolme
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:
 
1. Redistributions of source code must retain the above copyright
notice, this list of conditions and the following disclaimer.
 
2. Redistributions in binary form must reproduce the above copyright
notice, this list of conditions and the following disclaimer in the
documentation and/or other materials provided with the distribution.

3. Neither name of copyright holders nor the names of its contributors
may be used to endorse or promote products derived from this software
without specific prior written permission.


THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
``AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE REGENTS OR
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Warning: Some parts of PyVision may link to libraries using more 
restrictive licenses and some algorithms in PyVision by be covered 
under patents.  In these cases PyVision should display a warning
for commercial use.  If you believe this a warning should be added
for any algorithm or interface please contact me at
bolme@cs.colostate.edu
'''

__all__ = ['analysis','edge','face','optimize','other','point','types','vector']

WARN_COMMERCIAL_USE = True

def disableCommercialUseWarnings():
    '''
    Most of PyVision is released under the BSD license and
    can therefore be used free of charge in commercial 
    projects. In some limited cases PyVision uses algorithms
    that are covered by patents or source code released under
    copy left open source licenses such as GPL which may make
    software produced using those components unsuitable for 
    commercial distribution. 
    
    When a PyVision module contains or links to  non-commercial 
    code a warning message will be printed to stdout.  If you
    would like to disable these warning simply call this function
    before importing the offending module.  The users PyVision are 
    responsible for determining if their use of those components 
    respects all applicable licenses and patents.
    
    If you believe this a warning should be added for any algorithm 
    or interface please contact me at bolme@cs.colostate.edu 
    '''
    global WARN_COMMERCIAL_USE
    WARN_COMMERCIAL_USE = False

#Import basic pyvision types

#================================== Imports =====================================


from pyvision.types.img import Image

from pyvision.types.Point import Point

from pyvision.types.Rect import Rect,CenteredRect

from pyvision.types.Affine import AffineFromRect, AffineRotate, AffineTranslate, AffineNonUniformScale

from pyvision.util.normalize import meanUnit

from pyvision.util.windows import cosineWindow
