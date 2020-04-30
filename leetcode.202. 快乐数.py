"""
author: noc
time: 2020年4月30日
url: https://leetcode-cn.com/problems/happy-number/
"""
"""
solution：用一个集合来保存每一格数，由于一个快乐数最后总会形成1，那如果这个数不是一个快乐数，它在每次进行位数平方相加的同时，必然会形成一个循环，也就是说它最后
形成的数会遇见前面的数。
所以我们用一个集合来保存每次计算后的数。
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        def get_next(n):
            total_sum = 0
            while n > 0:
                n, d = divmod(n, 10)
                total_sum += d ** 2
            return total_sum
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)
        return n == 1

"""
快慢指针解法，与前面的相同，但是去掉了集合，也就是空间复杂度变为1，思路都是一样，不过这儿用快慢指针来判断，是否进入了一个循环中
"""
"""
class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            total_sum = 0
            while n > 0:
                n, d = divmod(n, 10)
                total_sum += d ** 2
            return total_sum
        fast_num = get_next(n)
        slow_num = n
        while n != 1 and fast_num != slow_num:
            fast_num = get_next(get_next(fast_num))
            slow_num = get_next(slow_num)
        return fast_num == 1
"""

if __name__ == '__main__':
    out = Solution().isHappy(19)
    print(out)