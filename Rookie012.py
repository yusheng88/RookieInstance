# -*- coding: utf-8 -*-
"""
https://www.runoob.com/python3/python3-odd-even.html Python 判断奇数偶数
"""

num = int(input("输入一个数字："))
if (num % 2) == 0:
    print("{0} 是偶数".format(num))
else:
    print("{0} 是奇数".format(num))