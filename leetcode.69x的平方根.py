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


class Solution:
    def sqrt(self, x):
        """
        数学分析法，牛顿迭代法：
        """
        ## 牛顿迭代法
        latest = 1
        curr = 0
        while True:
            curr = latest
            latest = (latest + x / latest) / 2  ## 迭代法公式
            if (abs(latest - curr) < 0.0000001):
                break

        return int(curr)
    def sqrt1(self, x):
        """
        二分法很好理解，要知道任何一个正整数的算术平方根是不可能大于这个数的一般的，所以基于这个特性，我们可以利用二分查找找[1, x / 2]那个数与x最接近。
        注意的是，我们找中位数的时候，要找右中位数, 因为当遇到x = 9的时候，我们计算到区间[3, 4]，如果此时去中位数按照以前mid = （left + right） // 2的话，
        此时mid = 3， 那么 mid * mid = 9 = x, 此时left = mid，区间始终在[3, 4]循环，所以要取右区间
        """
        ## 二分法
        if x == 0: return 0
        left, right = 1, x >> 1;
        while left < right:
            mid = (left + right + 1) >> 1
            v = mid * mid
            if v > x: right = mid - 1
            else: left = mid + 1
        return left

if __name__ == "__main__":
    x = 9
    out = Solution().sqrt1(x)
    print(out)