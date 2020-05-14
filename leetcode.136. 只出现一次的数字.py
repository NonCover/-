"""
author: noc
time: 2020年5月14日
url: https://leetcode-cn.com/problems/single-number/
"""
"""
按位异或：
每一位，相同为0， 不同为1
两个相同的数异或为0
任何一位数与0异或为它本身
"""

class Solution:
    def singleNumber(self, nums):
        a = nums[0]
        for i in range(1, len(nums)):
            a ^= nums[i]
        return a

if __name__ == '__main__':
    nums = [4, 2, 3, 2, 3]
    out = Solution().singleNumber(nums)
    print(out)