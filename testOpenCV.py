import numpy as npy
import cv2
import matplotlib.pyplot as plt

print("版本 =", cv2.__version__)
color_img = cv2.imread('C:\\Users\\13524\\Desktop\\641.jpg')
gray_img = cv2.cvtColor(color_img, cv2.COLOR_RGB2GRAY)
cv2.imshow("", color_img)
cv2.waitKey(1000)
cv2.imshow("", gray_img)
cv2.waitKey(1000)


for window in range(3, 999, 2):
    binary_img = cv2.adaptiveThreshold(gray_img, 676666, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, window, 2)
    cv2.imshow(window.__str__(), binary_img)
    cv2.waitKey(0)