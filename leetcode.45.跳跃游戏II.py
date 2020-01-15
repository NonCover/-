'''
给定一个非负整数数组，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
你的目标是使用最少的跳跃次数到达数组的最后一个位置。
示例:
输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
说明:
假设你总是可以到达数组的最后一个位置。
'''
# 贪心算法
class Solution:
    def jump(self, nums):
        if nums.count(1)==len(nums):return len(nums)-1
        steps, maxVal, end = 0, 0, 0
        for i in range(len(nums) - 1):
            maxVal = max(maxVal, nums[i] + i)   # 每一步的最大步数到达的位置
            if i == end:    # 到达每一步的边界，意味开始走下一步，步数加一
                end = maxVal
                steps += 1
            print(maxVal, end, steps)
        return steps

s = Solution()
print(s.jump([2,3,5,1,4]))