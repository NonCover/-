"""
author: noc
time: 2020年5月15日
url: https://leetcode-cn.com/problems/subarray-sum-equals-k/
"""

"""
字典保存数组的前缀和和前缀和的满足为k的个数。
当 sum - k 出现在字典中的keys，说明当前数组[sum - k + 1: sum + 1]的和 == k 
"""
class Solution:
    def sunArraySum(self, nums, k):
        dic = {}
        sum = 0
        ans = 0
        dic[0] = 1      ## 为了满足当第一个数 = k
        for num in nums:
            sum += num
            if dic.get(sum - k):
                ans += dic.get(sum - k)
            dic[sum] = dic.get(sum) + 1 if dic.get(sum) else 1
        print(dic)
        return ans

if __name__ == '__main__':
    nums = [1,1,1]
    k = 2
    out = Solution().sunArraySum(nums, k)
    print(out)