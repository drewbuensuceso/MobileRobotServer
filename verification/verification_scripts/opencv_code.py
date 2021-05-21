import re

from PIL import Image
import cv2
import numpy as np

import pytesseract as pytesseract
import os


class OpencvCode:
    def __init__(self, image_path=None):
        self.image_path = image_path
        
    def verify_image(self):
        try:
            img = cv2.imread(self.image_path, 0) #load image in grayscale
            resized_img = cv2.resize(img, None, fx=0.8, fy=0.8, interpolation=cv2.INTER_CUBIC)
            thresh = cv2.threshold(resized_img, 150, maxval=255, type=cv2.THRESH_BINARY)[1]
            th2 = cv2.medianBlur(thresh, 3)
            cv2.imwrite("thresholded_keyb.png",th2)
            data = pytesseract.image_to_string(th2, config="-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789 --oem 0 --psm 6 --tessdata-dir tessdata")
            print(data)
            msg="success"
            code=0
        except:
            data=0
            code = 1
            msg = "failed"
            print("image verification error")

        return [code,data,msg]

    def verify_pw_num(self, len, passwd):
        try:
            img = cv2.imread(self.image_path, 0) #load image in grayscale
            resized_im1 = cv2.resize(img, None, fx=0.8, fy=0.8, interpolation=cv2.INTER_CUBIC)
            thresh = cv2.threshold(resized_im1, 100, maxval=255, type=cv2.THRESH_BINARY_INV)[1]
            th2 = cv2.medianBlur(thresh, 5)
            keyboard = pytesseract.image_to_string(th2, config="-c tessedit_char_whitelist=0123456789 --oem 0 --psm 6 --tessdata-dir tessdata")
            cv2.imwrite("thresholded_keyboard.png",th2)
            print(keyboard)
            msg="success"
            code=0
        except:
            data=0
            code = 1
            msg = "failed"
            print("pw_num_error")

        return [code, data, keyboard, msg]

    def verify_pw_letter(self, len, passwd):
        try:
            img = cv2.imread(self.image_path, 0) #load image in grayscale
            resized_im1 = cv2.resize(img, None, fx=0.8, fy=0.8, interpolation=cv2.INTER_CUBIC)
            thresh = cv2.threshold(resized_im1, 150, maxval=255, type=cv2.THRESH_BINARY_INV)[1]
            th2 = cv2.medianBlur(thresh, 3)
            keyboard = pytesseract.image_to_string(th2, config="-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz --oem 0 --psm 6 --tessdata-dir tessdata") #can specify language here
            cv2.imwrite("thresholded_keyboard.png",th2)
            print(keyboard)
            msg="success"
            code=0
        except:
            data=0
            code = 1
            msg = "failed"
            print("pw_letter_error")
        
        return [code, data, keyboard, msg]

    def verify_pw_full_letter(self, len, passwd):
        try:
            img = cv2.imread(self.image_path, 0) #load image in grayscale
            resized_im1 = cv2.resize(img, None, fx=0.8, fy=0.8, interpolation=cv2.INTER_CUBIC)
            thresh = cv2.threshold(resized_im1, 150, maxval=255, type=cv2.THRESH_BINARY_INV)[1]
            th2 = cv2.medianBlur(thresh, 5)
            keyboard = pytesseract.image_to_string(th2, config="-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz --oem 0 --psm 6 --tessdata-dir tessdata")
            cv2.imwrite("thresholded_keyboard.png",th2)
            print(keyboard)
            msg="success"
            code=0
        except:
            data=0
            code = 1
            msg = "failed"
            print("pw_letter_error")
        
        return [code, data, keyboard, msg]


#def display_keybs(img1,img2):

    #BLACK_THRESHOLD =  150
    #THIN_THRESHOLD = 0
     #ANNOTATION_COLOUR = (222,0,222) #annotate on rows of keyboard, for future use

#    im1 = cv2.imread(img1,0)
#    resized_im1 = cv2.resize(im1, None, fx=0.8, fy=0.8, interpolation=cv2.INTER_CUBIC)
#    thresh = cv2.threshold(resized_im1, thresh=BLACK_THRESHOLD, maxval=255, type=cv2.THRESH_BINARY)[1]
#    th2 = cv2.medianBlur(thresh, 3)
#    keyb_string = pytesseract.image_to_string(th2, config="-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz --oem 0 --psm 6 --tessdata-dir tessdata")
#    cv2.imshow("keyboard",th2)
#    cv2.waitKey(0)
#    print(keyb_string)

    
    #im2 = cv2.imread(img2,0)
    #resized_im2 = cv2.resize(im2, None, fx=1.05, fy=1.05, interpolation=cv2.INTER_CUBIC)
    #cv2.imshow("keyb1", resized_im1)
    #cv2.imshow("keyb2", resized_im2)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    #     return()

#verify_pw_num(keyboard1, 0, 0)

#display_keybs(keyboard1, keyboard2)