#!/usr/bin/python
#-*- coding:utf-8 -*-
#__author__ = noc
#1.
'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]'''  #lang:python

import time

def Timer(twoSum):
    def wraper(nums, target):
        start  = time.time()
        twoSum(nums, target)
        end = time.time()
        print('执行时间:', end-start)
    return wraper

@Timer
def twoSum(nums, target):           #利用字典模拟哈希值求解
    dic = {}
    for index, num in enumerate(nums):
        # 如果字典存在该对象, 返回结果
        if dic.get(target - num) is not None: 
            res = [dic[target-num], index]
            print(res)
        dic[num] = index


if __name__ == "__main__":
    twoSum([3, 3, 4], 6)