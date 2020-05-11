"""
author: noc
time: 2020年5月11日
url: https://leetcode-cn.com/problems/powx-n/
"""
"""
快速幂， 判断幂的正负数
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        i = n
        while i != 0:
            if i % 2 != 0:      # 当幂为奇数时，取出一个无法进行相乘的数进行运算
                ans *= x
            x *= x
            i //= 2
        return ans if n > 0 else 1 / ans

if __name__ == '__main__':
    out = Solution().myPow(2, 31)
    print(out)