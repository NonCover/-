#!/usr/bin/python
#-*- coding:utf-8 -*-
#__author__ = noc
#18.
'''
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：

答案中不可以包含重复的四元组。

示例：

给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''
def fourSum(nums, target):
    nums.sort()
    print(nums)
    k, res = 0, []
    for k in range(len(nums) - 3):
        if k > 0 and nums[k] == nums[k-1]:continue  #去重
        i, j = k + 1, len(nums) - 1
        for i in range(i, len(nums) - 2):
            if i > k + 1 and nums[i] == nums[i-1]:continue
            last, j = i + 1, len(nums) - 1
            while last < j:
                s = nums[k] + nums[i] + nums[last] + nums[j]
                if s < target:
                    last += 1
                    while last < j and nums[last] == nums[last-1]:last+=1
                if s > target:
                    j -= 1
                    while last < j and nums[j] == nums[j+1]:j-=1
                if s == target:
                    res.append([nums[k], nums[i], nums[last], nums[j]])
                    last += 1
                    j -= 1  
                    while last < j and nums[last] == nums[last-1]:last+=1   #去重
                    while last < j and nums[j] == nums[j+1]:j-=1   #去重
    return res

print(fourSum([1,-2,-5,-4,-3,3,3,5], -11))