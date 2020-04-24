'''
author: noc
time: 2020年4月24日
url: https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/
'''

from typing import List
class Solution:
    count = 0
    def reversePairs(self, nums: List[int]) -> int:
        ## 分治法
        size = len(nums)
        tmp = [0 for _ in range(size)]
        self.mergeSort(nums, 0, size - 1, tmp)
        return self.count

    ## 前闭后闭
    def mergeSort(self, nums, start, end, tmp):
        if start >= end: return
        mid = start + (end - start) // 2
        self.mergeSort(nums, start, mid, tmp)
        self.mergeSort(nums, mid + 1, end, tmp)
        self.merge(nums, start, mid, end, tmp)

    def merge(self, nums, start, mid, end, tmp):
        idx, p1, p2 = start, start, mid + 1
        while (p1 <= mid and p2 <= end):
            if nums[p1] > nums[p2]:
                self.count = self.count + (mid - p1 + 1)
                tmp[idx] = nums[p2]
                p2 += 1
            else:
                tmp[idx] = nums[p1]
                p1 += 1
            idx += 1

        while p1 <= mid:
            tmp[idx] = nums[p1]
            idx += 1
            p1 += 1
        while p2 <= end:
            tmp[idx] = nums[p2]
            idx += 1
            p2 += 1
        for j in range(start, end + 1):
            nums[j] = tmp[j]

if __name__ == '__main__':
    nums = [7,5,6,4]
    out = Solution().reversePairs(nums)
    print(out)