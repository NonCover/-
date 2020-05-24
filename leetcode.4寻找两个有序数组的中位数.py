'''
author：noc
time：2020年5月24日
url：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
'''

"""
常规解法是将两个数组合在一起然后排序，最后返回中位值即可，但此时时间复杂度不合题意，另外，了解归并思想的可以利用双指针， 当两个指针一共移动了两个数组长度和+1 的一半次的时候，就说明到达中位数了，此时计算返回即可，但时间复杂度也
不符合条件，所以我们利用数组排好序的特征来做。
很明显，我们对于偶数的中位数而言，例如数组的长度为n，偶数的中位数为：（num[n // 2] + nums[n // 2 - 1]） / 2
对于奇数的中位数，我们直接取nums[n // 2]
同时对于中位数，其两边的个数一定相等，并且左边第一个数一定小于右边第一个数，题意两个数组都是排好序的，
那么这两个数组的中位数位置为：k = (m1 + m2 + 1) // 2
我们只需要从一个较短的数组中找到一个位置m1，其左边作为中位数的左边的数，其右边作为中位数的右边的数，另外一个数组位置 k - m1的左边作为中位数左边的数，其右边作为中位数右边的数，
那么就有 max(nums1[:m1] + nums2[:k - m1]) < min(nums1[m1:] + nums2[k - m1:]) 当然直接简化成 max(nums1[m1 - 1], nums2[k - m1 - 1]) < min(nums1[m1], nums2[k - m1])
同时要处理一下越界的情况  
"""
from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List, nums2: List) -> float:
        n1, n2 = len(nums1), len(nums2)
        if n1 > n2: return self.findMedianSortedArrays(nums2, nums1) ## 数组1始终要大于等于数组2，才能够利用二分法计算
        k = (n1 + n2 + 1) // 2
        left, right = 0, n1
        while left < right:
            m1 = left + (right - left) >> 1
            m2 = k - m1
            if nums1[m1] < nums2[m2 - 1]:
                left = m1 + 1
            else:
                right = m1
        m1 = left
        m2 = k - left
        c1 = max(nums1[m1 - 1] if m1 > 0 else float("-inf"),
                    nums2[m2 - 1] if m2 > 0 else float("-inf"))
        if (n1 + n2) & 1 == 1:
            return c1
        c2 = min(nums1[m1] if m1 < n1 else float("inf"),
                    nums2[m2] if m2 < n2 else float("inf"))
        return (c1 + c2) / 2

if __name__ == '__main__':
    nums1 = [1, 3]
    nums2 = [2]
    out = Solution().findMedianSortedArrays(nums1, nums2)
    print(out)