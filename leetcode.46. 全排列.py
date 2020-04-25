'''
author: noc
time: 2020年4月25日
url: https://leetcode-cn.com/problems/permutations/
'''
'''
典型的回溯法，先找到回溯出口，也就是满足长度符合条件后，即可回溯，把答案加入到答案数组中即可。
'''
from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs(n, size, s, li):
            if n == size:
                ans.append(li[:])   # 注意这里是引用拷贝, 我们要把li数组复制, 也就是返回一个新值
                return
            for i in range(size):
                if nums[i] not in s:
                    s.add(nums[i])
                    li.append(nums[i])
                    dfs(n + 1, size, s, li)
                    s.remove(nums[i])
                    li.pop()
        size = len(nums)
        dfs(0, size, set(), [])
        return ans

if __name__ == '__main__':
    nums = [1,2,3]
    out = Solution().permute(nums)
    print(out)