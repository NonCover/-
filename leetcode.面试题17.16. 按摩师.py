'''
@author：noc
@time：2020年3月24日
@url：https://leetcode-cn.com/problems/the-masseuse-lcci/
'''
'''
题解：这题是经典DP题的选与不选问题，由于我们不能选择相邻位置的两个值，所以我们用dp来保存每一步选或者不选当前nums[i]的值。由于nums的长度为 1或者为2时，我们只需要返回max（nums）即可，
所以我们直接用dp数组先保存nums[0]和nums[1]，dp[i]为前i个所选的最大值，我们通过max（dp[：i - 1]）可以求出，如果当前nums[i]的值要选的话，那么我们就需要找出[0, i - 1)的最大值，因为 i - 1 的值不能够选择，
以在对 max(dp[:i - 1]) + dp[i] 和 dp[i - 1]进行大小比较。最后dp[-1]就是我们的答案。我们可以优化一下空间复杂度，由于我们要保存前i步的最大值需要用dp数组来保存，这儿我们直接将值保存在nums里，用choose和
not_choose来保存当前值选与不选的最佳答案
时间复杂度：O（N）
空间复杂度：O（1）
'''
class Solution:
    def massage(self, nums):
        # l = len(nums)
        # if l == 0: return 0
        # if l <= 2: return max(nums)
        # dp = [nums[0], nums[1]]
        # for i in range(2, l):
        #     dp.append(nums[i])
        #     dp[i] = max(max(dp[:i - 1]) + dp[i], dp[i - 1])
        # return dp[-1]
        choose, not_choose = 0, 0
        for num in nums:
            po = choose
            choose = max(not_choose + num, choose)
            not_choose = max(not_choose, po)
        return max(choose, not_choose)
if __name__ == '__main__':
    nums = [2, 3,1 ,41, 2, 2]
    out = Solution().massage(nums)
    print(out)