'''
@author；noc
@time：2020年3月13日
@url：https://leetcode-cn.com/problems/majority-element/
'''


class Solution:
    def majorityElement(self, nums):
        '''
        1.Hash表
        max_count = len(nums) // 2  # 最大次数
        dic = {}
        for i in nums:
            if i in dic.keys():
                dic[i] += 1
            else:
                dic[i] = 1
        for i, j in dic.items():    # 迭代找出符合要求的 key
            if j > max_count:
                return i
        2.排序
        因为众数在数组中始终占据这样一半及以上的空间，当对数组排序后，数组 len（nums）// 2 位置的数一定是众数
        nums.sort()
        return nums[len(nums) // 2]
        '''
        # 3.多数投票算法
        '''
        遍历数组，给一个 候选值为 数组第一个值，并记这个值出现的次数为 count = 1
        当遍历的值与候选值相等时，count + 1，不相等，就减一
        如果 count 减到0时，就将候选值 判断为当前遍历的值，并继续遍历，判断
        总而言之就是 这个 数 位众数的话，那么这个数与其他不同的数抵消后，一定还有剩下的
        '''
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            else:
                if candidate == num:
                    count += 1
                else:
                    count -= 1
        return candidate

if __name__ == '__main__':
    out = Solution().majorityElement([3, 2, 3, 2, 3, 3, 4])
    print(out)
