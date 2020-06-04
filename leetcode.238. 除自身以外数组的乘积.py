"""
author: noc
time: 2020年6月4日
url: https://leetcode-cn.com/problems/product-of-array-except-self/
"""
from typing import List
"""
解法：
一个数组保存从前到后的乘积，另一个则是从后向前。
例如 计算 nums = {1，2，3，4}  
arr1 = {1, 2, 6, 24}
arr2 = {24, 24, 12, 4}
然后我们遍历一遍 nums，nums[i] = arr1[i - 1] * arr2[i + 2]，注意边界的判断。
为了节省空间，我们可以用输出数组来保存 arr2
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [0] * n
        output[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            output[i] = output[i + 1] * nums[i]
        r = 1      ## 前i个的乘积
        for i in range(n - 1):
            output[i] = r * output[i + 1]
            r *= nums[i]
        output[-1] = r
        return output

if __name__ == '__main__':
    nums = [1,2,0,4]
    out = Solution().productExceptSelf(nums)
    print(out)