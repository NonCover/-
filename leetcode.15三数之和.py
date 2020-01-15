#!/usr/bin/python
#-*- coding:utf-8 -*-
#__author__ = noc
#15.
'''
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
def threeSum(nums):
    threeNums = []
    nums.sort() #排序
    j, k = len(nums)-1, 0   #j，k分别指向nums最后一个和第一个的值
    for k in range(len(nums)-2):
        if nums[k] > 0: break   #当k指向的数大于0时，循环结束
        if k > 0 and nums[k] == nums[k-1]:continue  #去重
        i = k + 1
        j = len(nums) - 1   #while循环完后，右指针重新回到最右边
        while i < j:
            num = nums[k] + nums[i] + nums[j]
            if num < 0:
                i += 1
                while i < j and nums[i] == nums[i-1]:i+=1 #去重
            elif num > 0:
                j -= 1
                while i < j and nums[j] == nums[j+1]:j-=1   #去重
            else:
                threeNums.append([nums[k], nums[i], nums[j]])
                i += 1
                j -= 1  
                while i < j and nums[i] == nums[i-1]:i+=1   #去重
                while i < j and nums[j] == nums[j+1]:j-=1   #去重
    return threeNums
print(threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))