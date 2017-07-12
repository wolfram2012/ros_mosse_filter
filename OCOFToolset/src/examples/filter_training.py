# Copyright 2010, David S. Bolme, Colorado State University Research 
# Foundation
#
# Colorado State University Software Evaluation License Agreement
#
# This license agreement ("License"), effective today, is made by and between 
# you (hereinafter referred to as the "Licensee") and the Board of Governors of 
# the Colorado State University System acting by and through Colorado State 
# University, an institution of higher education of the State of Colorado, 
# located at Fort Collins, Colorado, 80523-2002 ("CSU"), and concerns certain 
# software described as "Correlation Filters for Detection, Recognition, and 
# Registration," a system of software programs for advanced video signal 
# processing and analysis. 
#
# 1.  General. A non-exclusive, nontransferable, perpetual license is granted 
#     to the Licensee to install and use the Software for academic, non-profit, 
#     or government-sponsored research purposes. Use of the Software under this 
#     License is restricted to non-commercial purposes. Commercial use of the 
#     Software requires a separately executed written license agreement. 
#    
# 2.  Permitted Use and Restrictions. Licensee agrees that it will use the 
#     Software, and any modifications, improvements, or derivatives to the 
#     Software that the Licensee may create (collectively, "Improvements") 
#     solely for internal, non-commercial purposes and shall not distribute, 
#     transfer, deploy, or externally expose the Software or Improvements to any 
#     person or third parties without prior written permission from CSU. The 
#     term "non-commercial," as used in this License, means academic or other 
#     scholarly research which (a) is not undertaken for profit, or (b) is not 
#     intended to produce works, services, or data for commercial use, or (c) is 
#     neither conducted, nor funded, by a person or an entity engaged in the 
#     commercial use, application or exploitation of works similar to the 
#     Software. 
#    
# 3.  Ownership and Assignment of Copyright. The Licensee acknowledges that 
#     CSU has the right to offer this copyright in the Software and associated 
#     documentation only to the extent described herein, and the offered 
#     Software and associated documentation are the property of CSU. The 
#     Licensee agrees that any Improvements made by Licensee shall be subject 
#     to the same terms and conditions as the Software. Licensee agrees not to 
#     assert a claim of infringement in Licensee copyrights in Improvements in 
#     the event CSU prepares substantially similar modifications or derivative 
#     works. The Licensee agrees to use his/her reasonable best efforts to 
#     protect the contents of the Software and to prevent unauthorized 
#     disclosure by its agents, officers, employees, and consultants. If the 
#     Licensee receives a request to furnish all or any portion of the Software 
#     to a third party, Licensee will not fulfill such a request but will refer 
#     the third party to the CSU Computer Science website 
#     http://www.cs.colostate.edu/~vision/ocof.html so that the third party's 
#     use of this Software will be subject to the terms and conditions of this 
#     License. Notwithstanding the above, Licensee may disclose any 
#     Improvements that do not involve disclosure of the Software. 
#     
# 4.  Copies. The Licensee may make a reasonable number of copies of the 
#     Software for the purposes of backup, maintenance of the Software or the 
#     development of derivative works based on the Software. These additional 
#     copies shall carry the copyright notice and shall be controlled by this 
#     License, and will be destroyed along with the original by the Licensee 
#     upon termination of the License. 
#     
# 5.  Acknowledgement. Licensee agrees that any publication of results obtained 
#     with the Software will acknowledge its use by an appropriate citation as 
#     specified in the documentation. 
#     
# 6.  Acknowledgment. CSU acknowledges that the Software executes patent pending 
#     Algorithms for the purpose of non-commercial uses. Licensee acknowledges 
#     that this Agreement does not constitute a commercial license to the 
#     Algorithms. Licensee may apply for a commercial license to the Algorithms 
#     from Colorado State University Research Foundation by visiting 
#     http://www.csuventures.org. 
#    
# 7.  Disclaimer of Warranties and Limitation of Liability. THE SOFTWARE IS 
#     PROVIDED "AS IS," WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
#     INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY 
#     AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. CSU MAKES NO 
#     REPRESENTATION OR WARRANTY THAT THE SOFTWARE WILL NOT INFRINGE ANY PATENT 
#     OR OTHER PROPRIETARY RIGHT. IN NO EVENT SHALL CSU BE LIABLE FOR ANY 
#     DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES 
#     (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
#     SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
#     CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT 
#     LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY 
#     OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF 
#     SUCH DAMAGE. 
#     
# 8.  Termination. This License is effective until terminated by either party. 
#     Your rights under this License will terminate automatically without notice 
#     from CSU if you fail to comply with any term(s) of this License. Upon 
#     termination of this License, you shall immediately discontinue all use of 
#     the Software and destroy the original and all copies, full or partial, of 
#     the Software, including any modifications or derivative works, and 
#     associated documentation. 
#    
# 9.  Governing Law and General Provisions. This License shall be governed by 
#     the laws of the State of Colorado, excluding the application of its 
#     conflicts of law rules. This License shall not be governed by the United 
#     Nations Convention on Contracts for the International Sale of Goods, the 
#     application of which is expressly excluded. If any provisions of this 
#     License are held invalid or unenforceable for any reason, the remaining 
#     provisions shall remain in full force and effect. This License is binding 
#     upon any heirs and assigns of the Licensee. The License granted to 
#     Licensee hereunder may not be assigned or transferred to any other person 
#     or entity without the express consent of the Regents. This License 
#     constitutes the entire agreement between the parties with respect to the 
#     use of the Software licensed hereunder and supersedes all other previous 
#     or contemporaneous agreements or understandings between the parties, 
#     whether verbal or written, concerning the subject matter. 

'''
This file contains source code needed to train ASEF and MOSSE eye detectors.
Training uses the csuScrapShot face database for training. This database 
was scanned from CSU year books from 1910-1920 so the images are of poor
quality.  In other words... This is example code that can be modified for 
use on your own data. You probably do not want to use the filters trained
on this database for eye detection purposes.  For a higher quality and 
pretrained eye detector follow this link. 
U{PyVision: Face Detection and Eye Localization<http://sourceforge.net/apps/mediawiki/pyvision/index.php?title=Face_Detection_and_Eye_Localization>}

Created on Oct 19, 2010

@author: bolme
'''

import pyvision as pv
import ocof
import os.path


if __name__ == '__main__':
    ilog = pv.ImageLog()
    
    # Setup paths to the CSU scrapshot face database
    SCRAPS_DIR = os.path.join(pv.__path__[0],'data','csuScrapShots')
    EYES_FILENAME = os.path.join(SCRAPS_DIR,"coords.txt")
    
    # Set the tilesize and eye locations
    TILE_SIZE = (128,128)
    LEFT_EYE  = pv.Point(40,64)
    RIGHT_EYE = pv.Point(88,64)

    eye_data_file = open(EYES_FILENAME)
    
    # Train ASEF and MOSSE Filters
    asef_filter = ocof.ASEF((128,128))
    mosse_filter = ocof.MOSSE((128,128))
    
    i = 0
    for line in eye_data_file:
        
        # Train on the first 80 faces
        i += 1
        if i > 80: break
        
        # Get information on the image filename and eye coordinates
        imname,lx,ly,rx,ry = line.split()
        print "Processing:",imname
        leye = pv.Point(float(lx),float(ly))
        reye = pv.Point(float(rx),float(ry))
        filename = os.path.join(SCRAPS_DIR,imname+'.pgm')
        
        # Read the image
        im = pv.Image(filename)
        
        # Add 4 perturbations per input image
        for p in range(4):
            
            # Compute an affine transform for the training images
            affine = pv.AffinePerturb(0.1,3.14/16,4,TILE_SIZE)*pv.AffineFromPoints(leye,reye,LEFT_EYE,RIGHT_EYE,TILE_SIZE)
            
            # Transform the image and the left eye coordinate
            tile = affine(im)
            pt = affine(leye)
            
            # log the training images
            tile.annotatePoint(pt,color='yellow')
            ilog(tile,"TrainingImage")
            
            # add to filter training and log intermediate images to ilog
            asef_filter.addTraining(tile,pt,ilog=ilog)
            mosse_filter.addTraining(tile,pt,ilog=ilog)
    
    # finish filter training
    asef_filter.train()
    mosse_filter.train()
    
    # log images of the filters
    ilog(asef_filter.asImage(),"ASEF_FILTER")
    ilog(mosse_filter.asImage(),"MOSSE_FILTER")
    
    # save the filters to the log.  These can be reloaded using pickle
    ilog.pickle(asef_filter,"ASEF_FILTER")
    ilog.pickle(mosse_filter,"MOSSE_FILTER")

    # Run the filter on testing data
    i = 0
    for line in eye_data_file:
        i += 1
        if i > 80: break
        
        # Read filename and eye data
        imname,lx,ly,rx,ry = line.split()
        print "Processing:",imname
        leye = pv.Point(float(lx),float(ly))
        reye = pv.Point(float(rx),float(ry))
        filename = os.path.join(SCRAPS_DIR,imname+'.pgm')
        
        # Load image
        im = pv.Image(filename)
        
        # Only test on one perturbation

        # Compute an affine transform for the training images
        affine = pv.AffinePerturb(0.1,3.14/16,4,TILE_SIZE)*pv.AffineFromPoints(leye,reye,LEFT_EYE,RIGHT_EYE,TILE_SIZE)
        
        # Transform the image 
        tile = affine(im)
        
        # Use the filters to locate the eyes
        
        # Show the correlation output
        corr = asef_filter.correlate(tile)
        corr = corr*(corr>0.0)
        ilog(pv.Image(corr),'ASEF_CORRELATION')
        
        # Locate the eye
        pt = asef_filter.locate(tile)
        
        # Show the correlation
        tile.annotateCircle(pt,radius=3,color='red')
        corr = mosse_filter.correlate(tile)
        corr = corr*(corr>0.0)
        ilog(pv.Image(corr),'MOSSE_CORRELATION')

        #Locate the eye
        pt = mosse_filter.locate(tile)
        tile.annotateCircle(pt,radius=7,color='green')
        ilog(tile,"TestingImage")
    
    ilog.show()            
