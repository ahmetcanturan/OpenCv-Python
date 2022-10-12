#-*- coding: utf-8 -*-

import cv2
import time
import numpy as np

"""
sudo apt-get install python-opencv
sudo apt-get install python-matplotlib
"""

"""
http://stackoverflow.com/a/32929315
https://pythontips.com/2015/03/11/a-guide-to-finding-books-in-images-using-python-and-opencv/
http://docs.opencv.org/3.1.0/d2/d96/tutorial_py_table_of_contents_imgproc.html
http://stackoverflow.com/questions/10533233/opencv-c-obj-c-advanced-square-detection
"""

##################
DELAY = 0.02
USE_CAM = 0
IS_FOUND = 0

MORPH = 11
CANNY = 250
##################
# 420 x 590 oranı 210mm x 297mm gerçek boyuttaki kağıt için
_width  = 210.0*2
_height = 297.0*2

# 600 x 470 oranı 100mm x 78mm gerçek boyuttaki kağıt için
_width  = 100.0*6
_height = 78.0*6

_margin = 0.0
##################

if USE_CAM: video_capture = cv2.VideoCapture(0)

corners = np.array(
	[
		[[  		_margin, _margin 			]],
		[[ 			_margin, _height + _margin  ]],
		[[ _width + _margin, _height + _margin  ]],
		[[ _width + _margin, _margin 			]],
	]
)

pts_dst = np.array( corners, np.float32 )

def rotate( image, angle, center = None, scale = 1.0 ):
	( h, w ) = image.shape[:2]
	if center is None: center = ( w / 2, h / 2 )
	# Perform the rotation
	M = cv2.getRotationMatrix2D( center, angle, scale )
	rotated = cv2.warpAffine( image, M, ( w, h ), flags = cv2.INTER_CUBIC )
	return rotated

while True :

	if USE_CAM :
		ret, rgb = video_capture.read()
	else :
		ret = 1
		rgb = cv2.imread("b.jpg", 1)

		rgb = cv2.resize( rgb, ( 1024, 768 ) )

	if ( ret ):

		gray = cv2.cvtColor( rgb, cv2.COLOR_BGR2GRAY )

		gray = cv2.bilateralFilter( gray, 2, 10, 120 )

		edges  = cv2.Canny( gray, 10, CANNY )

		kernel = cv2.getStructuringElement( cv2.MORPH_RECT, ( MORPH, MORPH ) )

		closed = cv2.morphologyEx( edges, cv2.MORPH_CLOSE, kernel )

		contours, h = cv2.findContours( closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE )


		for cont in contours:

			# Küçük alanları pass geç
			print (cv2.contourArea( cont ))
			if cv2.contourArea( cont ) > 5000 :

				arc_len = cv2.arcLength( cont, True )

				approx = cv2.approxPolyDP( cont, 0.1 * arc_len, True )

				if ( len( approx ) == 4 ):
					IS_FOUND = 1
					#M = cv2.moments( cont )
					#cX = int(M["m10"] / M["m00"])
					#cY = int(M["m01"] / M["m00"])
					#cv2.putText(rgb, "Center", (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 3)
					print (approx)
					"""
					[
						[[847 204]]
						[[316 205]]
						[[316 624]]
						[[861 620]]
					]
					"""

					pts_src = np.array( approx, np.float32 )

					h, status = cv2.findHomography( pts_src, pts_dst )
					out = cv2.warpPerspective( rgb, h, ( int( _width + _margin * 2 ), int( _height + _margin * 2 ) ) )

					cv2.drawContours( rgb, [approx], -1, ( 255, 0, 0 ), 2 )

				else : pass

		#cv2.imshow( 'closed', closed )
		#cv2.imshow( 'gray', gray )
		cv2.imshow( 'edges', edges )
		cv2.imshow( 'rgb', rgb )

		if IS_FOUND :
			#pass
			out = rotate( out, 180 )
			cv2.imshow( 'out', out )
			#current = str( time.time() )
			current = "1"
			cv2.imwrite( 'ocvi10_' + current + '_crop.jpg', out )
			print ("saved 1")

		if cv2.waitKey(27) & 0xFF == ord('q') :
			break

		if cv2.waitKey(99) & 0xFF == ord('c') :
			#current = str( time.time() )
			current = "1"
			cv2.imwrite( 'ocvi_' + current + '_edges.jpg', edges )
			cv2.imwrite( 'ocvi_' + current + '_gray.jpg', gray )
			cv2.imwrite( 'ocvi_' + current + '_org.jpg', rgb )
			print ("Pictures saved")

		time.sleep( DELAY )

	else :
		print ("Stopped")
		break


cv2.destroyAllWindows()

# end