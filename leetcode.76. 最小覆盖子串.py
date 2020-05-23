"""
author: noc
time: 2020年5月23日
url: https://leetcode-cn.com/problems/minimum-window-substring/
"""
"""
滑动窗口：
两个指针，left和right。[left, right]相当于一个窗口，s[left：right]一个符合条件的答案。
needs字段来记录需要出现的字符，window来记录当前窗口出现需要出现字符的个数。
一开始，我们移动right指针向右滑动，直到滑动到我们窗口符合条件后，在滑动left指针，left指针向左滑动的时候，
我们不断更新答案，直到找到一个最小长度并且符合条件的窗口。
"""
import collections
class Solution(object):
    def minWindow(self, s: str, t: str) -> str:
        needs = collections.defaultdict(int)
        window = collections.defaultdict(int)
        for c in t: needs[c] += 1
        start, minLen = 0, 0xfffffff    ## 更新答案
        left, right = 0, 0  ## 滑动指针
        match = 0   ## 用来记录当前窗口需要出现的字符达到条件的个数
        while right < len(s):
            c1 = s[right]
            if c1 in needs.keys():
                window[c1] += 1
                if window[c1] == needs[c1]: ## 当前c1字符达到了条件，记录
                    match += 1
            right += 1
            while match == len(needs):  ## 说明当前窗口全部达到条件
                c2 = s[left]
                if right - left < minLen:   ## 更新
                    start = left
                    minLen = right - left
                if c2 in needs.keys():
                    window[c2] -= 1     ## 不断缩小窗口，更新答案
                    if window[c2] < needs[c2]:  ## 当前窗口已经不满足条件了
                        match -= 1    ## 将会跳出缩小窗口循环，开始滑动right指针，直到退出
                left += 1
        return s[start: start + minLen]

if __name__ == '__main__':
    s = "ADOBECODEBANC"
    t = "ABC"
    out = Solution().minWindow(s, t)
    print(out)

