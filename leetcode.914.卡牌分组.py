'''
@author：noc
@time：2020年3月27日
@url：https://leetcode-cn.com/problems/x-of-a-kind-in-a-deck-of-cards/
'''

'''
题解：利用最大公因数求出每组牌组的个数，因为要求牌组个数相同，且个数必须大于等于2。所以解法如下：
1. 用哈希表保存每张牌的个数
2. 用辗转相除法求最大公因数
3. 判断最大公因数是否大于等于2
'''
import collections
from functools import reduce
import math

class Solution:
    def hasGroupsSizeX(self, deck):
        cnt = collections.Counter(deck)
        return reduce(math.gcd, cnt.values()) >= 2

if __name__ == '__main__':
    deck = [2, 2, 3, 3, 4, 4]
    out = Solution().hasGroupsSizeX(deck)
    print(out)