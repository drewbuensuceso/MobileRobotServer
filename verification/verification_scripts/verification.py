import cv2
import pytesseract
import cv2
import re
import numpy as np
from opencv_code import OpencvCode
import log_server as log

def verification(target_device, vc_img):
    cv_code = OpencvCode(vc_img)
    data = cv_code.verify_image()
    log.verification(vc_img, data.data, target_device.accountAlias, target_device.device_id, target_device.ip_address, target_device.trans_time)
    return data

def verify_pw_num(target_device, keyb_img, len, passwd):
    #device_info = device info coming from Termux application
    cv_code = OpencvCode(keyb_img)
    data = cv_code.verify_pw_num(len, passwd)
    log.keyboard(keyboardImg=keyb_img, code=passwd, position=data.data, accountAlias=target_device.accountAlias, \
        target_device=target_device.device_id, ip_address = target_device.ip_address, transTime=target_device.transTime)
    return data

def verify_pw_letter(target_device, pw_letter_img,len,passwd):
    #device_info = device info coming from Termux application
    cv_code = OpencvCode(pw_letter_img)
    data = cv_code.verify_pw_letter(len, passwd)
    log.keyboard(keyboardImg=pw_letter_img, code=passwd, position=data.data, accountAlias=target_device.accountAlias, \
        target_device=target_device.device_id, ip_address = target_device.ip_address, transTime=target_device.transTime)
    return data

def verify_pw_full_letter(target_device, pw_full_letter_img, len, passwd):
    #device_info = device info coming from Termux application
    cv_code = OpencvCode(pw_full_letter_img)
    data = cv_code.verify_pw_full_letter(len, passwd)
    log.keyboard(keyboardImg=pw_full_letter_img, code=passwd, position=data.data, accountAlias=target_device.accountAlias, \
        target_device=target_device.device_id, ip_address = target_device.ip_address, transTime=target_device.transTime)
    return data