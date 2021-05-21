import cv2
import pytesseract
import cv2
import re
import numpy as np
from opencv_code import OpencvCode

def verification(vc_img):
    cv_code = OpencvCode(vc_img)
    data = cv_code.verify_image(cv_code)
    return data

def verify_pw_num(keyb_img, len, passwd):
    cv_code = OpencvCode(keyb_img)
    data = cv_code.verify_pw_num(cv_code)
    return data

def verify_pw_letter(pw_letter_img,len,passwd):
    cv_code = OpencvCode(pw_letter_img)
    data = cv_code.verify_image(cv_code)
    return data

def verify_pw_full_letter(pw_full_letter_img, len, passwd):
    cv_code = OpencvCode(pw_full_letter_img)
    data = cv_code.verify_image(cv_code)
    return data