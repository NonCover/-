"""
author: noc
time: 2020年5月20日
urL: https://leetcode-cn.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/
"""

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        ## 记录每个状态的下标
        pre = [-1] * 32
        ## 一开始所有元音的状态都为0,所以对应的下标为-1
        pre[0] = -1
        ans, curr = 0, 0    ## curr用来记录每次的状态 位上1表示奇数 0表示偶数
        for i, c in enumerate(s):       # 每个元音字母的对应位置
            """按位异或，如果出现偶数次字母的话 异或为0，奇数则为1"""
            if c == 'a': curr ^= 1      # 00001
            elif c == 'e': curr ^= 2    # 00010
            elif c == 'i': curr ^= 4    # 00100
            elif c == 'o': curr ^= 8    # 01000
            elif c == 'u': curr ^= 16   # 10000
            ## 记录当前状态对应的下标
            if (pre[curr] == -1): pre[curr] = i
            else: ans = max(ans, i - pre[curr])
            print(curr, pre[curr], ans)
        return ans

if __name__ == '__main__':
    s = "eleet"
    out = Solution().findTheLongestSubstring(s)
    print(out)