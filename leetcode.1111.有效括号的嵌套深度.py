'''
@author:noc
@time:2020年4月1日
@url:https://leetcode-cn.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/
'''
'''
题解：一开始对于此题我是完全懵逼的，描诉不清的题。看了题解我才明白表达的啥意思。总是此题的意思是，将一组括号分别分成 A B两个子序列，然后A + B后形成的新序列的括号潜逃深度保持最小。
基于此我明白了，遍历序列，使两个连续的“（”或“）”不能连续出现在同一子序列中，通过奇偶来判断‘（’的应该出现在哪一个子序列中。
时间复杂度：O（n） n为序列的数据量
空间复杂度：O（1）除返回数组外
'''
class Solution:
    def maxDepthAfterSplit(self, seq):
        ret = []
        d = 0
        for s in seq:
            if s == '(':
                d += 1
                ret.append(d % 2)
            else:
                ret.append(d % 2)
                d -= 1
        return ret

if __name__ == '__main__':
    seq = '(())()'
    out = Solution().maxDepthAfterSplit(seq)
    print(out)