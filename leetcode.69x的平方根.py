#!/usr/bin/python
#-*- coding:utf-8 -*-
#__author__ = noc
#69.
'''
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:

输入: 4
输出: 2
示例 2:

输入: 8
输出: 2
说明: 8 的平方根是 2.82842..., 
     由于返回类型是整数，小数部分将被舍去。
'''         #Lang:python
import time

def Timer(mySqrt):
    def runTime(x):
        start = time.time()
        mySqrt(x)
        end = time.time()
        print('运行时间:', end-start)

    return runTime
@Timer
def mySqrt(x:int) -> int:
    last = 1
    cur = 0
    while  True:
        cur = last
        last = (last + x / last) / 2            #牛顿迭代法     x=(x0 + a/x0)/2 求与x轴的焦点
        if abs(cur - last) < 0.000006:
            print('%s的平方根为%s'%(x, int(last)))
            break

if __name__ == "__main__":
    mySqrt(8)