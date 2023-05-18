import numpy as np
import cv2
from tkinter import *

def draw_circle(img, x, y, color_name):
    h,w = img.shape[:2]
    cr = int(min(h,w)*0.015)
    color = [0,0,255] if color_name == 'red' else [255,0,0] # bgr

    for r in range(cr+1):
        for dy in range(-r, r+1):
            if 0 <= y+dy < h:
                dx = r - abs(dy)
                if 0 <= x+dx < w:
                    img[y+dy, x+dx] = color
                if 0 <= x-dx < w:
                    img[y+dy, x-dx] = color
