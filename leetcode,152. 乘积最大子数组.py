"""
author: noc
time: 2020年5月18日
url: https://leetcode-cn.com/problems/maximum-product-subarray/
"""

"""
动态规划：
由于我们的数组里存在负数，所以当我们计算最大值的时候，有可能遇到负数，让最大值变成最小值，最小值变成最大值
所以我们需要维护两个数imax和imin，这两个数分别维护当前下标下的最大值和最小值
"""
class Solution:
    from typing import List
    def maxProduct(self, nums: List) -> int:
        if (len(nums) == 0): return 0
        ans, imax, imin = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            mx, mn = imax, imin
            ## 状态转移方程
            imax = max(mx * nums[i], nums[i], mn * nums[i])
            imin = min(mx * nums[i], nums[i], mn * nums[i])
            ans = max(imax, ans)
        return ans

if __name__ == '__main__':
    nums = [2,3,-2,4]
    out = Solution().maxProduct(nums)
    print(out)