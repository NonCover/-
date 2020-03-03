# @author: noc
# @time: 2020年3月3日14点59分
# @heaf： https://leetcode-cn.com/problems/sorted-merge-lcci/

class Solution(object):
    def merge(self, A, m, B, n):
        '''
        逆序指针，遍历，比较两个数组值，将最大的值，放入对于数组A的指针位置
        '''
        pA, pB, tail = m - 1, n - 1, m + n - 1
        while pA >= 0 or pB >= 0:
            if pA == -1:
                A[tail] = B[pB]
                tail -= 1
                pB -= 1
            elif pB == -1:
                A[tail] = A[pA]
                pA -= 1
                tail -= 1
            elif A[pA] >= B[pB]:
                A[tail] = A[pA]
                tail -= 1
                pA -= 1
            else:
                A[tail] = B[pB]
                tail -= 1
                pB -= 1

if __name__ == "__main__":
    A, m = [1, 2, 3, 0, 0, 0], 3
    B, n = [2, 4, 5], 3
    print(A)
    ret = Solution().merge(A, m, B, n)
    print(A)