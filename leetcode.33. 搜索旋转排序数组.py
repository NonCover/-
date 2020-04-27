"""
author: noc
time: 2020年4月27日
url: https://leetcode-cn.com/problems/search-in-rotated-sorted-array/
"""
"""
二分法，对于常规二分法是用来搜寻有序数组的，而这里给出的是有序数组经过某点旋转而来的，对于这样的数组观察会发现一个规律，那就是从 nums[0, mid) 和 nums(mid, len(nums) - 1] 
这两段一定是有一个数组是有序的，另一个无序或者有序，我们只需要判断一段数组是否有序，如果有序的话，就判断 target是否在这段当中，如果不是到另外一段去找
例如：[4, 5, 6, 7, 0, 1, 2]    
如果target在[4, 5, 6, 7]中，r = mid - 1
如果target在[0, 1, 2]中, l = mid + 1     当然无论target值为多少，我们首先应该在有序的数组中先去找，nums[0] <= target < nums[mid]这样才能直到target在不在其中，如果不在，肯定在另外一个
"""
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[-1]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

if __name__ == '__main__':
    nums = [4,5,6,7,0,1,2]
    target = 6
    out = Solution().search(nums, target)
    print(out)