'''
author:noc
time:2020年4月10日
url:https://leetcode-cn.com/problems/letter-case-permutation/
'''
'''
非递归解法很明显比递归解法思路更加清晰，举例：‘a2b’  temp保存的是S[0, idx]的可能性，char需要保存S，以便我们在下一次中能够精确的更新temo的可能
'''
class Solution:
    def letterCasePermutation(self, S):
        ret = []
        N = len(S)
        # def dfs(idx, item):
        #     if idx == N or len(item) == N:
        #         ret.append(item)
        #         return
        #     elif S[idx].isdigit():
        #         dfs(idx + 1, item + S[idx])
        #     elif S[idx].isupper():
        #         dfs(idx + 1, item + S[idx])
        #         dfs(idx + 1, item + S[idx].lower())
        #     else:
        #         dfs(idx + 1, item + S[idx])
        #         dfs(idx + 1, item + S[idx].upper())
        # dfs(0, '')
        # return ret

        temp = []
        char = ['']
        for idx in range(N):
            if S[idx].isdigit():
                for c in char:
                    temp.append(c + S[idx])
            elif S[idx].isupper():
                for c in char:
                    temp.append(c + S[idx].lower())
                    temp.append(c + S[idx])
            elif S[idx].islower():
                for c in char:
                    temp.append(c + S[idx].upper())
                    temp.append(c + S[idx])
            char = temp
            temp = []
        return char

if __name__ == '__main__':
    S = '123asd'
    out = Solution().letterCasePermutation(S)
    print(out)