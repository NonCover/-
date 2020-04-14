'''
author: noc
time: 2020年4月14日
url: https://leetcode-cn.com/problems/number-of-ways-to-paint-n-x-3-grid/
'''
'''
up-write：这题一开始我是蒙蔽的，因为我想到的三色问题，四色问题，但是与此题无关。最后才发面这题其实很简单，复杂问题简单化。ok！
根据官方demo1，RGY三种颜色无论怎么组合（符合条件下）都满足 ABA、ABC三种方式。然后我们再扩展一下思想，当有2 * N个方格时，
ABA 下面的组合方式有： BAB BAC BCB CAB CAC
ABA 下面的组合方式有： BAB BCB CAC CAB
所以得出的结论有：
 1.ABA下的  ABA类型有3个 ABC类型有2个： 总数 = ABA * 3 + ABC * 2
 2.ABC下的  ABA类型有2个 ABC类型有2个： 总数 = ABA * 2 + ABC * 2
 
 排列方式个数 = ABA总数 + ABC总数
 
 完美解决！            
'''
class Solution:
    def numOfWays(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 12   # 处理特殊数
        aba, abc = 6, 6
        for i in range(2, n + 1):
            aba, abc = 3 * aba + 2 * abc, 2 * aba + 2 * abc
        ret = aba + abc
        return ret % 1000000007

if __name__ == '__main__':
    n = 7
    out = Solution().numOfWays(n)
    print(out)