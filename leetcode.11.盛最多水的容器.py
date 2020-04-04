'''
@author:noc
@time:2020年4月4日
@url:https://leetcode-cn.com/problems/container-with-most-water/
'''
'''
题解：双指针
'''
class Solution:
    def maxArea(self, height: list[int]) -> int:
        ret = 0
        i, j = 0, len(height) - 1   # 双指针
        while i != j:
            ret = max(ret, min(height[i], height[j]) * (j - i)) # 更新最大面积
            if height[i] >= height[j]:
                j -= 1
            else:
                i += 1
        return ret