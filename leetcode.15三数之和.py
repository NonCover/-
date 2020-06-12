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

"""
题解：
    简单的三指针操作，首先对数组进行排序，然后定义指针 k 遍历数组从 0 到 倒数第二个，
    i 指针指向 k + 1， j 指针指向最后一个。
    定义变量 s 保存 nums[k] + nums[i] + nums[j]，由于数组是排好序的，所以当 s < 0 的时候，就增加 i 指针，
    s > 0 的时候，就减小 j 指针，注意我们还要处理 数据重复，相邻两个数据相同的话，只计算一个就行了 
"""


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