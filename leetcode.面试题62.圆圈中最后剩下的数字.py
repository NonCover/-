'''
@author：noc
@time：2020年3月30日
@url：https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/
'''

'''
最优解发：参考约瑟夫环问题，因为我们删除至剩下一个数时，这个数必然在数组的 0 位置，然后我们可以反推出这个位置在一开始的位置，这个位置就是最终答案
'''
class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        ret = 0
        for i in range(2, n + 1):
            ret = (ret + m) % i         # 反推公式，每次我们删除的数是上一次删除数在数 3个，那么我们 +3 在对当前数组取模就是上一次的位置。
        return ret


if __name__ == '__main__':
    out = Solution().lastRemaining(10, 17)
    print(out)