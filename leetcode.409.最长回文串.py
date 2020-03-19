'''
@author：noc
@time：2020年3月19日
@url：https://leetcode-cn.com/problems/longest-palindrome/
'''

import collections

'''
题解：题目本身很简单，一开始就想到了利用Hash来存储每个字母出现的次数，并查看每一个值，如果值为偶数，则代表该值能够在回文串里面左右出现次数相等，
ret 就可以加上这个数的次数，当然如果是奇数的话，这个数不能左右相等，只能加上 这个数的次数 -1，但是回文串是偶数的话，如果要构成最长回文串，如果
还有没有用完的字母，则可以放在中间，ret + 1.
例如： baaabaaab > baaaab 
'''

class Solution(object):
    def longestPalindrome(self, s):
        if not s: return 0
        s_cnt = collections.Counter(s)
        ret = 0
        for v in s_cnt.values():
            ret += v // 2 * 2
            if ret % 2 == 0 and v % 2 == 1:
                ret += 1
        return ret

if __name__ == '__main__':
    s = "ababababa"
    out = Solution().longestPalindrome(s)
    print(out)