#!/usr/bin/env python
import numpy as np
import cv2

DIM=(640, 480)

K=np.array([[325.1564515669869, 0.0, 318.97813943722116], [0.0, 321.50468917410274, 249.05011600944852], [0.0, 0.0, 1.0]])

D=np.array([[0.4567841421603866], [-2.375800551358405], [4.190925078868009], [-2.8322958563831335]])

def undistort_image(img):
    
    #Calcula mapas que resuelve la distorsion y rectifica con remap()
    map1, map2 = cv2.fisheye.initUndistortRectifyMap(K, D, np.eye(3), K, DIM, cv2.CV_16SC2)
    #Transforma la imagen a quitar efecto ojo de pez
    undistorted_img = cv2.remap(img, map1, map2, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)
    return undistorted_img

