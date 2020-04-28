"""
author: noc
time: 2020年4月28日
url: https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof/
"""
"""
位运算，由于异或运算对于 不相同的位取1 相同的取0  所以对于只有两个数只出现一次的数组而言，所有数异或后一定 等于 这两个数的异或
1. 先对这个数组进行异或， ret 保存的是 a ^ b （a, b 为答案）
2. 在找到ret中的某一位为1的index 例如 ret = B0100 div = B0100    ret = B0101 div= B0001 or B0100   
3. 在进行分组，将相同的分同一组，不同的数分不同组，如何判断 nums[i] & div
"""
from typing import List

class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        ret = 0
        for num in nums:
            ret ^= num
        div = ret & -ret
        print(ret)
        # while div & ret == 0:
        #     div <<= 1
        print(div)
        a, b = 0, 0
        for num in nums:
            if num & div:
                a ^= num
            else:
                b ^= num
        return [a, b]

if __name__ == '__main__':
    nums = [4, 6, 2, 2, 6, 0]
    out = Solution().singleNumbers(nums)
    print(out)