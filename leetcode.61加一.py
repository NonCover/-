#!/usr/bin/python
#-*- coding:utf-8 -*-
#__author__ = noc
#66.                    
'''
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:

输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
示例 2:

输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。
'''             #Lang:python


import time

def Timer(calculation):
    def wraper(listVal):
        start  = time.time()
        calculation(listVal)
        end = time.time()
        print('执行时间:', end-start)
    return wraper

@Timer
def calculation(listVal):
    tmp = 1
    n = len(listVal) - 1
    for i in range(n, -1, -1):
        # 将列表倒叙迭代
        if tmp == 0:    
            break
        if i == 0 and listVal[i] + tmp == 10:   #如果当索引到0，并且加 1 为 10 的话就在前面加个 1 ， listVal[0] = 1, 长度len(listVal) + 1
            listVal[i] = 0
            listVal = [1] + listVal
            continue
        cur = listVal[i] + tmp  
        listVal[i] = cur % 10
        tmp = cur // 10
    print(listVal)

if __name__ == "__main__":
    a = [1, 3, 5, 9]
    calculation(a)