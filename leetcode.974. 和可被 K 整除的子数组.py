"""
author: noc
time: 2020年5月27日
url: https://leetcode-cn.com/problems/subarray-sums-divisible-by-k/
"""

"""
前缀和问题：只要遇到数组求子数组个数某某问题，一般都要用到前缀和，这里求数组是否存在一个子树组与K的模等于0。
我们数组P[i] = 前i个数的和，A[i + 1]...A[j]的和 = P[j] - P[i], 同时如果 （P[j] - P[i]） % K == 0 的话，
就说明该子数组成立，根据同余定理，P[i] % K == P[j] % K 的，所以我们要求当前前缀是否有子数组的话，只需要计算当前前缀和对 K 取模的值，
是否存在其他前缀对 K 取模与其相等。所以我们利用哈希表来存放。键 = 前缀和对 K 取模，值 = 当前前缀和满足条件的子数组个数。
"""

import collections
from typing import List
class Solution:
    def subarraysDivByK(self, A: List, K: int) -> int:
        d = collections.defaultdict(int)
        d[0] = 1        ## 处理 A[i] % K == 0 的情况
        ans, presum = 0, 0
        for n in A:
            presum += n     ## 前缀和
            mod = presum % K
            cnt = d[mod]    ## 找到是否有与当前前缀与K的模相等的键，如果没有将会默认取 0
            ans += cnt
            d[mod] = cnt + 1    ## 更新
        return ans

if __name__ == '__main__':
    A = [4, 5, 0, -2, -3, 1]
    K = 5
    output = Solution().subarraysDivByK(A, K)
    print(output)
