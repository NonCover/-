"""
author: noc
time: 2020年6月15日
url: https://leetcode-cn.com/problems/subsets/
"""

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        N = len(nums)
        def helper(idx, curr):
            ans.append(curr + [])
            for i in range(idx, N):
                curr.append(nums[i])
                helper(i + 1, curr)
                curr.pop()
        helper(0, [])
        return ans

if __name__ == '__main__':
    nums = [1, 2, 3]
    out = Solution().subsets(nums)
    print(out)