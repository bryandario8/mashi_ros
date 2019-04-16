#!/usr/bin/env python
import sys
import numpy as np
import cv2

import undistort as ud
import realzado

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

#cont = 0

class image_preprocesor:
 
	def __init__(self):
	    self.image_pub = rospy.Publisher("/mashi_ros/image_topic",Image,queue_size=5)
	    self.bridge = CvBridge()
	    self.image_sub = rospy.Subscriber("/usb_cam/image_raw",Image,self.callback)

	def callback(self,data):
	    #global cont
	    try:
	        cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
	    except CvBridgeError as e:
	        print(e)
	    #if(cont%15==0):
	    (rows,cols,channels) = cv_image.shape
	    m = cv2.getRotationMatrix2D(((cols-1)/2.0, (rows-1)/2.0), 90, 1)
	    cv_image = cv2.warpAffine(cv_image, m, (cols, rows))
	
	    cv_image= ud.undistort_image(cv_image)
	    cv_image = realzado.realzado(cv_image)
	    #rospy.loginfo(cont)	        
	    #cv2.imshow("Image window", cv_image)
	    #cv2.waitKey(3)

	    try:
	        self.image_pub.publish(self.bridge.cv2_to_imgmsg(cv_image, "bgr8"))
	    except CvBridgeError as e:
	        print(e)
	    #cont+=1
	
def main(args):
	#global _cont   
	ip = image_preprocesor()
	rospy.init_node('mashi_ros')
	try:
	   rospy.spin()
	except KeyboardInterrupt:
	   print("Shutting down")
	cv2.destroyAllWindows()

if __name__ == '__main__':
	main(sys.argv)

