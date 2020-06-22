# -*- coding: utf-8 -*-
"""
    作者：小卜
    功能：角度识别
    版本：v1.0
    日期：2020/04/01

"""
import cv2
import numpy as np


def main():
    path = 'C://Users/dell/Desktop/test.jpg'
    pic = cv2.imread(path, 0)

    # pic = Remove_line(pic, 5)
    # cv2.imshow('111', pic)
    # cv2.waitKey(0)
    # for i in range(w):
    #     pic[0, i] = [255]*3
    #     pic[h-1, i] = [255]*3
    # for j in range(h):
    #     pic[j, 0] = [255]*3
    #     pic[j, w-1] = [255]*3
    # 去除边缘
    contours, hierarchy = cv2.findContours(pic, 2, 2)
    # 寻找轮廓
    for cnt in contours:

        center_point = cv2.minAreaRect(cnt)[0]
        # 中心点坐标
        width, height = cv2.minAreaRect(cnt)[1]
        # 轮廓宽度和高度
        if width*height > 225:
            rect = cv2.minAreaRect(cnt)
            box = cv2.boxPoints(rect)
            # 获取最小外接矩形的4个顶点
            box = np.int0(box)
            if 0 not in box.ravel():
                for i in range(4):
                    cv2.line(pic, tuple(box[i]), tuple(box[(i + 1) % 4]), 1)
                # cv2.drawContours(pic, [box], 0, (255, 0, 0), 5)
                cv2.imshow('111', pic)
                cv2.waitKey(0)
                angle = cv2.minAreaRect(cnt)[2]
                print(angle)
                x_f = round((center_point[0]), 3)
                y_f = round((center_point[1]), 3)
                center_point_t = (x_f, y_f)
                print(center_point_t)


if __name__ == '__main__':
    main()

