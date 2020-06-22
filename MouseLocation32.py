# -*- coding: utf-8 -*-
"""
    作者：小卜
    功能：鼠标键盘控制word
    版本：v1.0
    日期：2019/07/21

"""
import pyautogui
try:
    while True:
        x, y = pyautogui.position()
        print(x, y)
except KeyboardInterrupt:
    print('\nExit.')