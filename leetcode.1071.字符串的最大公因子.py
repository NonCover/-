'''
@author: noc
@time: 2020年3月12日
@url: https://leetcode-cn.com/problems/greatest-common-divisor-of-strings/
'''
import math
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        s1, s2 = len(str1), len(str2)
        max_len = math.gcd(s1, s2)      # 利用辗转相除法求出最大公因子的长度
        max_str = str1[: max_len]       # 切出 str1 或 str2 的 前max_len 就是他们的最大公因子
        if str1 + str2 == str2 + str1:
            # 例如：'ABCABC' + 'ABC' = "ABC" + "ABCABC"    成立
            #       'ABABAB' + 'AC' = 'AC' + 'ABABAB'   不成立
            return max_str
        return ''

if __name__ == '__main__':
    out = Solution().gcdOfStrings('ABABAB', 'AB')
    print(out)