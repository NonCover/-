'''
author: noc
time: 2020年4月10日
url: https://leetcode-cn.com/problems/combination-sum/
'''
'''
dfs
'''
class Solution:
    def combinationSum(self, candidates, target):
        ret = []
        N = len(candidates)
        def helper(idx, aux, sum_aux):
            if idx == N or sum_aux > target: return # 剪枝
            if sum_aux == target:   # 满足条件
                ret.append(aux)
                return

            helper(idx, aux + [candidates[idx]], sum_aux + candidates[idx]) #
            helper(idx + 1, aux, sum_aux)
        helper(0, [], 0)
        return ret

if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    target = 7
    out = Solution().combinationSum(candidates, target)
    print(out)