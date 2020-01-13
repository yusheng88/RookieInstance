# -*- coding: utf-8 -*-
"""
https://www.runoob.com/python3/python-simplestopwatch.html
Python 实现秒表功能
"""

import time


print('按下回车开始计时，按下Ctrl + c 停止计时')

while True:

    input("")
    starttime = time.time()
    print('开始', starttime)
    try:
        while True:
            print('计时: ', round(time.time() - starttime, 0), '秒', end="\r")
            time.sleep(1)
    except KeyboardInterrupt:
        print('结束')
        endtime = time.time()
        print('总共的时间为:', round(endtime - starttime, 2), 'secs')
        break
