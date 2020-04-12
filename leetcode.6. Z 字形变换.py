'''
author: noc
time: 2020年4月12日
url: https://leetcode-cn.com/problems/zigzag-conversion/
'''
'''
首先我们要明确得是，给你一个字符串，我们按照从上到下，从左到右得去排序，然后我们再依次一排一排得将每一个字符保存到结果中，
同时我们需要处理一些特殊情况例如字符串无法完整排出 Z 字，或多或少得情况下，我们再第31行处理。
'''

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        ret = ''
        N = len(s)
        i = 0
        linePoor = 2 * numRows - 2
        while i < numRows:
            j = i
            while j < N:
                print(i, j)
                if i == 0 or i == numRows - 1:
                    ret += s[j]
                elif j == i:
                    ret += s[i]
                else:
                    ret += s[j - i * 2]
                    ret += s[j]
                j += linePoor

                if j - i * 2 < N and j >= N and j - i * 2 != j - linePoor:
                    ret += s[j - i * 2]


            i += 1

        return ret

if __name__ == '__main__':
    s = "AB"
    numRows = 1
    out = Solution().convert(s, numRows)
    print(out)