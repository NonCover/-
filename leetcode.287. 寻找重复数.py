"""
author: noc
time: 2020年5月26日
url: https://leetcode-cn.com/problems/find-the-duplicate-number/
"""
from typing import List

"""
佛洛依德算法: 根据题目条件。数组里的值一定出现在闭区间 1 到 n，由于数组里只有一个数重复，其他数都是单独的，所以我们可以将这个数组
看成一个图，并且这个图里一定存在一个环，我们需要通过快慢指针来找大这个环，这里由于我们需要找到环入口，所以用佛洛依德算法求解
"""
class Solution:
    def findDuplicate(self, nums: List):
        slow, fast = 0, 0
        while True:
            slow = nums[slow]   ## 慢指针。每次走一步
            fast = nums[nums[fast]] ## 快指针 走两步
            if fast == slow:    ## 找到环相遇点（这里不一定是环的入口）
                break
        slow = 0    ## 慢指针重新从起点开始走
        while True:
            slow = nums[slow]
            fast = nums[fast]
            if fast == slow:    ## 环入口
                break
        return fast