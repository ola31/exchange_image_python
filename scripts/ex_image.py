#!/usr/bin/env python


import sys, time
import numpy as np
#from scipy.ndimage import filters
import cv2
import roslib
import rospy

from cv_bridge import CvBridge
from sensor_msgs.msg import CompressedImage
from sensor_msgs.msg import Image

bridge = CvBridge()

image_pub = rospy.Publisher("/output/image_raw/compressed", CompressedImage, queue_size = 1)

def image_listen():
    rospy.init_node('image_feature', anonymous=True)
   
    #subscriber = rospy.Subscriber("/camera/color/image_raw",Image, callback, queue_size = 1)
    subscriber = rospy.Subscriber("/usb_cam_arm/image_raw",Image, callback, queue_size = 1)

    rospy.spin()

def callback(data_):

    #frame = bridge.imgmsg_to_cv2(data_, "bgr8")
    frame = bridge.imgmsg_to_cv2(data_, "mono8")
    encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90]
    
        
    im = cv2.resize(frame, (208, 117))
    msg = bridge.cv2_to_compressed_imgmsg(im)  
    image_pub.publish(msg)

       

'''if __name__ == '__main__':
    main(sys.argv)'''

if __name__ == '__main__':
    image_listen()

