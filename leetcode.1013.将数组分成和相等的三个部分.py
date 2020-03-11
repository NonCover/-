'''
@author: noc
@time: 2020年3月11日
@url: https://leetcode-cn.com/problems/partition-array-into-three-parts-with-equal-sum/
'''

class Solution(object):
    def canThreePartsEqualSum(self, A):
        tie = sum(A)  # 和
        if tie % 3 != 0: return False   # 不能够对3整除的话 说明无法分成三份
        count, s = 0, 0
        for a in A:
            s += a
            if s == tie / 3:
                count += 1
                s = 0
            if count == 3:
                return True
        return False



if __name__ == "__main__":
    out = Solution().canThreePartsEqualSum([1,-1,1,-1])
    print(out)