"""
author: noc
time: 2020年6月6日
url: https://leetcode-cn.com/problems/longest-consecutive-sequence/
"""
"""
解法：
    用 set 去重，然后我们每次判断当前值 x 的 x + 1, x + 2...x + y是否在集合中，如果在，说明当前子序列的长度为 y + 1，
    当然为了防止进行重复的运算，我们需要判断 x - 1是否在集合中，如果在的话，x 的值肯定是进行过查看的。
    类似并查集一样，判断一个值是否在一个连续子序列中，只需要判断这个值的上级节点，也就是 x - 1 是否在集合中，
    如果不在的话，可以想象一下，这肯定是两个不同的子序列。
"""

from typing import List
class Solution:
    def longestConsecutive(self, nums: List) -> int:
        nums_set = set(nums)
        ans = 0
        for num in nums_set:
            if num - 1 not in nums_set:
                curr = 1
                while num + 1 in nums_set:
                    curr += 1
                    num += 1
                ans = max(ans, curr)
        return ans

if __name__ == '__main__':
    nums = [100, 4, 200, 1, 3, 2]
    out = Solution().longestConsecutive(nums)
    print(out)