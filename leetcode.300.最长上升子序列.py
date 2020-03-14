'''
@authot：noc
@time：2020年3月14日
@url：https://leetcode-cn.com/problems/longest-increasing-subsequence/
'''

class Solution(object):
    def lengthOfLIS(self, nums):
        '''
        动态规划，定义 dp【i】为 前i个最长上升子序列，
        我们从小到大依次遍历数组的值，计算 dp【i】的值时，我们要知道dp【0：i-1】的值
        状态转移方程 dp【i】== max（dp【0：i-1】） + 1，
        当遍历到 nums【i】时，需要再去遍历一遍 nums【0：i】，如果 nums【i】 > nums【0 -》 j】
        就将 nums【i】放在上升子序列后面
        由于循环里有一层循环 所以时间复杂度为 O（n**2）
        '''
        # dp = [] # 保存前i个最长上升子序列的长度
        # for i in range(len(nums)):
        #     dp.append(1)    #
        #     for j in range(0, i):
        #         if nums[i] > nums[j]:
        #             dp[i] = max(dp[i], dp[j] + 1)
        # print(dp)
        # return max(dp)
        '''
        动态规划 + 贪心思想
        定义一个数组 d， d[i] 表示数组长度为i的上升子序列的最小值,
        我们照样从前向后的遍历数组，d[0] = nums[0]
        遍历到 nums[j] 时，如果这个值比 d[-1]的值还大的话，就加入到后面
        如果这个值，比 d[-1]小的话，就用二分查找去找d中比这个数第一小的值，再将这个值后面的值更新为 nums[j]
        d 的值可能不是最长上升子序列，但他的长度确是最长上升子序列的长度
        '''
        if not nums: return 0
        d = []
        for i in nums:
            if not d or i > d[-1]:
                d.append(i)
            else:
                l, r = 0, len(d) - 1
                while l <= r:
                    mid = (l + r) // 2
                    if d[mid] >= i:
                        loc = mid
                        r = mid - 1
                    else:
                        l = mid + 1
                d[loc] = i
        return len(d)


if __name__ == '__main__':
    out = Solution().lengthOfLIS([1,3,6,7,9,4,10,5,6])
    print(out)