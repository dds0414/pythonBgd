# -*- coding: utf-8 -*-
import cv2
import numpy as np


def IMGRecognition(IMGPath):
    image = cv2.imread(IMGPath)
    print image.shape
    # grayMat = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # binMat = 255 - grayMat
    # np.savetxt("a.txt", binMat)
    # print binMat

# def setImage(image):
#     # 灰度处理
#     grayMat = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     # 反转并去噪
#     binMat = 255 - grayMat
#     for indexRow, i in enumerate(binMat):
#         for index, n in enumerate(i):
#             if n < 25:
#                 binMat[indexRow][index] = 0
#     # 去边缘
#     row, col = guiyi(binMat)
#     one = binMat[row[0]:row[-1], col[0]:col[-1] + 1]
#     # resize
#     res = cv2.resize(one, (30, 32), Image.ANTIALIAS)
#     # 归一化
#     data = res.reshape((1, 960))[0]
#     return data, res

if __name__ == u"__main__":
    IMGRecognition("bgd/test.jpg")
