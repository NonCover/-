#!/usr/bin/python
#-*- coding:utf-8 -*-
#__author__ = noc
#9.
'''
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
'''
class Solution:
    def isPalindromic(self, x: int) -> bool:
        if x < 0 and (x > 0 or x % 10 == 0):
            return False
        else:
            res = 0
            x1 = x
            while x1:
                res *= 10
                res += x1 % 10
                x1 //= 10
            return res == x
if __name__ == "__main__":
    print(Solution().isPalindromic(12321))