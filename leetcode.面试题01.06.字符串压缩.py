'''
@author：noc
@time：2020年3月16日
@url：https://leetcode-cn.com/problems/compress-string-lcci/
'''

'''
题解：简单的题，一开始自己写了一下，发现和算法题解运行速度满了一倍，才发现，自己的代码里对了太多没必要的运算，比如 len() 之类的
    照样时间复杂度只有O（n），遍历一遍数组，用 a 保存当前字符的长度，ch 保存当前字符，当遇到 S{i} ！= ch 时，就讲 ch + str{a}添加到答案中
    并且将 ch更新成 S[i]
'''
class Solution(object):
    def compressString(self, S):
        a = 0
        ret = ''
        ch = S[0]
        for i in S:
            if i == ch:
                a += 1
            else:
                ret += ch + str(a)
                a = 0
                ch = i
        ret += ch + str(a)
        return ret if len(ret) < len(S) else S

if __name__ == '__main__':
    S = "aabcccccaa"
    out = Solution().compressString(S)
    print(out)