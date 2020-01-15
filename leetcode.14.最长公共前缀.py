#@Author=noc @level=容易
'''
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。
示例 1:
输入: ["flower","flow","flight"]
输出: "fl"
示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。'''
class Solution:
    def longestCommonPrefix(self, strs):
        s = list(map(set, zip(*strs)))
        res = ''
        for i, j in enumerate(s):
            j = list(j)
            if len(j) < 2:
                res += j[0]
            else: break
        return res
s = Solution()
print(s.longestCommonPrefix(["flower","alow","flight"]))