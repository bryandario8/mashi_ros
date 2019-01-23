# -*- coding: utf-8 -*-
import cv2
import numpy as np
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def stretch(pixel, mini, maxi):
    return (pixel-min_i)*(max_o-min_o)/(max_i-min_i)+min_o

def shrink(pixel, mini, maxi, mins, maxs):
    return (max_s-min_s)*(pixel-min_i)/(max_i-min_i)+min_s

def realzado(image):
    img = image   #carga imagen de entrada
    rows, cols, ch = img.shape
    b,g,r = cv2.split(img)
    equ_b = cv2.equalizeHist (b)
    equ_g = cv2.equalizeHist (g)
    equ_r = cv2.equalizeHist (r)
    '''
    #Filtro Paso-Bajo
    blur_b = cv2.blur(b, (5,5))
    blur_g = cv2.blur(g, (5,5))
    blur_r = cv2.blur(r, (5,5))
    #shrink image
    shrink_img_b = np.zeros((int(rows),int(cols)), dtype='uint8')
    shrink_img_g = np.zeros((int(rows),int(cols)), dtype='uint8')
    shrink_img_r = np.zeros((int(rows),int(cols)), dtype='uint8')
    for x in range(rows):
        for y in range(cols):
            shrink_img_b[x,y]=shrink(blur_b[x,y],30, 240,30,150)
            shrink_img_g[x,y]=shrink(blur_g[x,y],30, 240, 30, 150)
            shrink_img_r[x,y]=shrink(blur_r[x,y],30, 240, 30, 150)
    #Subtract
    img_subtract_b = cv2.subtract(b, shrink_img_b)
    img_subtract_g = cv2.subtract(g, shrink_img_g)
    img_subtract_r = cv2.subtract(r, shrink_img_r)
    #Stretch
    stretch_img_b = np.zeros((int(rows),int(cols)), dtype='uint8')
    stretch_img_g = np.zeros((int(rows),int(cols)), dtype='uint8')
    stretch_img_r = np.zeros((int(rows),int(cols)), dtype='uint8')
    for x in range(rows):
         for y in range(cols):
             stretch_img_b[x,y]=stretch(img_subtract_b[x,y], 0, 100)
             stretch_img_g[x,y]=stretch(img_subtract_g[x,y], 0, 100)
             stretch_img_r[x,y]=stretch(img_subtract_r[x,y], 0, 100)
    '''
    return cv2.merge((equ_b,equ_g,equ_r))
