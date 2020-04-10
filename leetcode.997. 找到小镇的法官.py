'''
author: noc
time: 2020年4月10日
url：https://leetcode-cn.com/problems/find-the-town-judge/
'''
'''
题解：两个数组 trustNum[i] = i + 1这个人相信别人的个数 betrustNum[i] = i + 1被别人相信的个数,法官成立的条件为 trustNum[i] == 0, betrustNum[i] = N - 1
'''

class Solution:
    def findJudge(self, N, trust):
        # for i in range(1, N + 1):
        #     count = N
        #     for t in trust:
        #         if t[0] == i:
        #             count = N
        #             break
        #         elif t[0] != i and t[1] == i:
        #             count -= 1

        #     if count == 1: return i

        # return -1
        trustNum = [0] * N
        betrustNum = [0] * N
        for t in trust:
            trustNum[t[0] - 1] += 1
            betrustNum[t[1] - 1] += 1
        for i in range(N):
            if trustNum[i] == 0 and betrustNum[i] == N - 1:
                return i + 1
        return -1

if __name__ == '__main__':
    N = 3
    trust = [[1,3],[2,3],[3,1]]
    out = Solution().findJudge(N, trust)
    print(out)