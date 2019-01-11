#!/usr/bin/env python
from __future__ import print_function

import roslib
#roslib.load_manifest('my_package')
import sys
import rospy
import numpy as np
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from distutils.version import LooseVersion 
if LooseVersion(cv2.__version__).version[0]==3:


	class image_converter:
	 
		def __init__(self):
		    self.image_pub = rospy.Publisher("image_topic_2",Image,queue_size=255)
		    self.bridge = CvBridge()
		    self.image_sub = rospy.Subscriber("/usb_cam/image_raw",Image,self.callback)


		def undistort_image(self,img):
		    DIM=(640, 480)

		    K=np.array([[325.1564515669869, 0.0, 318.97813943722116], [0.0, 321.50468917410274, 249.05011600944852], [0.0, 0.0, 1.0]])

	            D=np.array([[0.4567841421603866], [-2.375800551358405], [4.190925078868009], [-2.8322958563831335]])
		    #Calcula mapas que resuelve la distorsion y rectifica con remap()
		    map1, map2 = cv2.fisheye.initUndistortRectifyMap(K, D, np.eye(3), K, DIM, cv2.CV_16SC2)
		    #Transforma la imagen a quitar efecto ojo de pez
		    undistorted_img = cv2.remap(img, map1, map2, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)
		    return undistorted_img

		def callback(self,data):
		    try:
		        cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
		    except CvBridgeError as e:
		        print(e)
	 	    (rows,cols,channels) = cv_image.shape
		    m = cv2.getRotationMatrix2D(((cols-1)/2.0, (rows-1)/2.0), 90, 1)
		    cv_image = cv2.warpAffine(cv_image, m, (cols, rows))

		    cv_image=self.undistort_image(cv_image)
		    
		    #cv2.imshow("Image window", cv_image)
		    #cv2.waitKey(3)

		    try:
		        self.image_pub.publish(self.bridge.cv2_to_imgmsg(cv_image, "bgr8"))
		    except CvBridgeError as e:
		       print(e)
		
	def main(args):
		ic = image_converter()
		rospy.init_node('image_converter', anonymous=True)
		try:
		   rospy.spin()
		except KeyboardInterrupt:
		   print("Shutting down")
		cv2.destroyAllWindows()

	if __name__ == '__main__':
		main(sys.argv)

