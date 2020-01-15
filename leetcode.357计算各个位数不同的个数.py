#!/usr/bin/env python
#-*- coding:utf-8 -*-
#__author__ = noc
#7.计算位数不同的个数 Lang:python
##描述:
# 利用动态规划求出没个位数不同的个数,记住这是一道排列组合的题##
'''
n = 0: 1
n = 1: 10
n = 2: 9 * 9 + (n = 1)
n = 3: 9 * 9 * 8 + (n = 2)
n = 4: 9 * 9 * 8 * 7 + (n = 3) 
'''

class solution:
    def countNumber(n):
        if not n :return 1
        res, m = 10, 9  # res计算得是每一个位数不同的个数，m返回的是需要每一位的可能的个数
        for i in range(1, n):                
            m *= 10 - i
            res += m
        return res
print(solution.countNumber(2))