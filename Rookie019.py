# -*- coding: utf-8 -*-
"""
https://www.runoob.com/python3/python3-fibonacci-sequence.html  Python 斐波那契数列
"""

import pysnooper


@pysnooper.snoop()
def FeBo():
    # 获取用户输入
    nterms = int(input("你需要几项？"))

    # 第一项和第二项
    n1 = 0
    n2 = 1
    count = 2

    # 判断输入的值是否合法
    if nterms <= 0:
        print("请输入一个正确的整数。")
    elif nterms == 1:
        print("斐波那契数列：")
        print(n1)
    else:
        print("斐波那契数列：")
        print(n1, ",", n2, end=' , ')
        while count < nterms:
            nth = n1 + n2
            print(nth, end=" , ")
            # 更新值
            n1 = n2
            n2 = nth
            count += 1


if __name__ == '__main__':
    FeBo()
