'''
@author:noc
@time:2020年4月9日
@url:https://leetcode-cn.com/problems/generate-parentheses/
'''

'''
dfs遍历，最好理解的一种解法，我们可以利用系统栈来模拟dfs
'''


class Solution:
    def generateParenthesis(self, n):
        self.ret = []
        def dfs(cur_str, lcount, rcount):
            if lcount == 0 and rcount == 0: # 当括号用完时，加入到结果数组中
                self.ret.append(cur_str)
                return
            if lcount > rcount: # 左边括号剩下的数大于右边，就不能够组成有效的括号组合
                return
            if lcount > 0:
                dfs(cur_str + '(', lcount - 1, rcount)
            if rcount > 0:
                dfs(cur_str + ')', lcount, rcount - 1)
        dfs('', n, n)
        print(self.ret)
        return self.ret

if __name__ == '__main__':
    n = 3
    Solution().generateParenthesis(n)
