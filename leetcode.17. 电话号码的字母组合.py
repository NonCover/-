'''
author: noc
time: 2020年4月10日
url：https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/
'''


class Solution:
    def letterCombinations(self, digits):
        if digits == '': return []
        letterCase = {
            '2': 'abc', '3': 'def', '4': 'ghi',
            '5': 'jkl', '6': 'mno', '7': 'pqrs',
            '8': 'tuv', '9': 'wxyz'
        }
        # 非递归
        # ret = []
        # temp = ['']
        # N = len(digits)
        # for idx in range(N):
        #     for letter in letterCase[digits[idx]]:
        #         for tp in temp:
        #             ret.append(tp + letter)
        #     temp = ret
        #     ret = []
        # return temp

        # 递归
        ret = []
        N = len(digits)

        def dfs(idx, item):
            if idx == N:
                ret.append(item)
                return
            for letter in letterCase[digits[idx]]:
                dfs(idx + 1, item + letter)

        dfs(0, '')
        return ret

if __name__ == '__main__':
    digist = '23'
    out = Solution().letterCombinations(digist)
    print(out)