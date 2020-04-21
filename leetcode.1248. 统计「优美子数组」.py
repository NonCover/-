'''
author: noc
time: 2020年4月21日
url: https://leetcode-cn.com/problems/count-number-of-nice-subarrays/
'''
from typing import  List
'''
暴力解法，遍历每一种情况，符合条件就 加一，数据过大就ac不了。
法二：其实这题我们不难发现规律，我们不需要去管偶数，只需要去管奇数即可。
我们先用一个数组来保存每一个奇数的下标，然后我们拿出k个连续的奇数的下标，我们只需要统计 k个连续奇数的右边的偶数个数，和左边的偶数个数即可
ans = 左边偶数个数+1 x 右边偶数个数+1
时间/空间复杂度：O(N)
'''
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # self.ans = 0
        # size = len(nums)
        # def nmsl(idx, k):
        #     if nums[idx] % 2 == 1: k -= 1
        #     if k < 0: return
        #     if k == 0:
        #         self.ans +=1
        #     for i in range(idx + 1, size):
        #         nmsl(i, k)
        #         return      ## 连续得子数组。每次回溯这儿也要回溯
        # for i in range(size):
        #     nmsl(i, k)
        # return self.ans
        size = len(nums)
        ## 存放奇数的下标
        # ans = 0
        # odd = [-1]
        # for i in range(size):
        #     if nums[i] % 2 == 1:
        #         odd.append(i)
        # odd.append(size)
        # for i in range(1, len(odd) - k):
        #     ans += ((odd[i] - odd[i - 1]) * (odd[i + k] - odd[i + k - 1]))
        # return ans
        cnt = [0] * (len(nums) + 1)
        cnt[0] = 1
        odd, ans = 0, 0
        for num in nums:
            if num & 1:
                odd += 1
            if odd >= k:
                ans += cnt[odd - k]
            cnt[odd] += 1
            print(cnt, ans)
        return ans

if __name__ == '__main__':
    nums = [1,1,2,1,1]
    k = 3
    out = Solution().numberOfSubarrays(nums, k)
    print(out)