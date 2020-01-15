'''
给定一个非负整数数组，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个位置。
示例 1:
输入: [2,3,1,1,4]
输出: true
解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。
示例 2:
输入: [3,2,1,0,4]
输出: false
解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。
'''
class Solition:
    def canJump(self, nums):
        if nums[0] == 0 and len(nums) > 1: return False
        if nums.count(0) == len(nums): return True
        maxVal = 0      # 跳跃的最大步数位置
        for i in range(len(nums) - 1): 
            if maxVal >= i and i + nums[i] > maxVal:    # 当maxVal小于该位置时，则代表当前的位置无法走到
                maxVal = i + nums[i]    # 刷新跳跃的最大步数位置
        return maxVal >= len(nums) - 1

s = Solition()
print(s.canJump([1, 0, 1, 0]))