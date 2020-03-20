'''
@author：noc
@time：2020年3月20日
@url：https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/solution/
'''
'''
Top K问题
我一开始首先想到的是 sort排序一遍，在返回出前K个数组，然而如果是在面试，可能直接就被pass了。后来想到前K大的值，我们可以利用堆排序来做
'''

import heapq

class Solution(object):
    def getLeastNumbers(self, arrs, k):
        if k == 0: return []
        hp = [-x for x in arrs[:k]]
        heapq.heapify(hp)
        for a in range(k, len(arrs)):
            if hp[0] < -arrs[a]:
                heapq.heappop(hp)
                heapq.heappush(hp, -arrs[a])
        ret = [-x for x in hp]
        return ret

if __name__ == '__main__':
    arrs = [2, 4, 1, 5, 6]
    k = 3
    out = Solution().getLeastNumbers(arrs, k)
    print(out)