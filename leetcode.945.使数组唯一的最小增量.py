'''
@author：noc
@time：2020年3月22日
@url：https://leetcode-cn.com/problems/minimum-increment-to-make-array-unique/
'''
'''
解法1：排序后遍历数组，先对A进行排序，然后遍历数组，用curr_max保存上一个数， 当A[i] 大于上一个数的话，就要一直加1，直到比上一个数大，也就是要增加 上一个数减去当前数加1 个1
时间复杂度为排序的复杂度O（nlogn） 空间复杂度O(1)
解法2：计数排序，用一个数组统计数字i出现的个数 count{i] = i，然后当 count[i] > 1的话，就当前的数加一，也就是 count[i] - 1, count[i + 1] + 1，当然我们一直要算到count[i] = 0
当然如果出现数组A全为1的情况下，他的长度会变为原先的两倍
时间复杂度O（n + k）空间复杂度O(k)
'''
import collections
class Solution:
    def minIncrementForUnique(self, A):
        # A.sort()    # 排序
        # curr_max = -1
        # ret = 0
        # for i in range(len(A)):
        #     if A[i] <= curr_max:
        #         ret += curr_max + 1 - A[i]
        #         A[i] = curr_max + 1
        #     curr_max = max(curr_max, A[i])
        ret = 0
        count = [0] * 80000
        for i in A:
            count[i] += 1
        for i in range(80000):
            if count[i] > 1:
                ret += count[i] - 1
                count[i + 1] += count[i] - 1
        return ret

if __name__ == '__main__':
    A = [1,2,2, 3]
    out = Solution().minIncrementForUnique(A)
    print(out)