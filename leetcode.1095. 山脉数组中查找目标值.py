"""
author: noc
time: 2020年4月29日
url: https://leetcode-cn.com/problems/find-in-mountain-array/
"""

"""
solution: 其实这题很简答，标准的二分查找模板，唯一需要注意的是，我们要在一个moutain数组里找值，我们先找到山顶，因为山顶将数组分成升序和降序两个数组，
找到山顶后，我们分别在左侧和右侧找，找到了就返回。没找到继续找。
1. 先找山顶
2. 找左侧数组
3. 找右侧数组
"""

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """

class MountainArray:
    def __init__(self, arr):
        self.arr = arr
        self.len = len(arr)
    def get(self, index: int) -> int:
        return self.arr[index]
    def length(self) -> int:
        return self.len

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray'):
        N = mountain_arr.length()
        l, r = 0, N - 1
        while l <= r:
            mid = (l + r) >> 1
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                l = mid + 1
            elif mountain_arr.get(mid) >= mountain_arr.get(mid + 1):
                r = mid - 1
            print(l, r)
        ## 定位到峰值
        l1, r1 = 0, l - 1
        l2, r2 = l, N - 1
        # 在左侧寻找
        while l1 <= r1:
            mid = (l1 + r1) >> 1
            x = mountain_arr.get(mid)
            if x == target:
                return mid
            if x < target:
                l1 = mid + 1
            elif x >= target:
                r1 = mid - 1
        ## 在右侧寻找
        while l2 <= r2:
            mid = (l2 + r2) >> 1
            x = mountain_arr.get(mid)
            if x == target:
                return mid
            if x < target:
                r2 = mid - 1
            elif x >= target:
                l2 = mid + 1
        return -1

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 1]
    ma = MountainArray(arr)
    target = 3
    out = Solution().findInMountainArray(target, ma)
    print(out)