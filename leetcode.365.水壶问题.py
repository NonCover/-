'''
@author：noc
@time：2020年3月21日
@url：https://leetcode-cn.com/problems/water-and-jug-problem/
'''

import math

'''
题解1: 贝祖定理：ax + by = c，若 a b 都为整数，那么 gcd（a, b）对于任意的一组 x，y的整数解，则 c一定是 gcd（a, b）的倍数，反过同样，c不为它的倍数，则无整数解。
同样对于此题的要求是：
装满任意一个水壶
清空任意一个水壶
从一个水壶向另外一个水壶倒水，直到装满或者倒空
不可能存在两个桶同时为 空 满的状态，所以水的变化只能是 多了 x 或 y， 少了 x或y。根据这一特性，我们可以求 ax + by = z的解了。
时间复杂度:O(logN) 取决于辗转相除法所求组大公因数的时间
空间复杂度:O(1)

题解2：利用深度搜索（dfs）来一次检查每一种情况，一旦找到某一种情况符合条件，则返回结果.
根据允许的条件可以看出，一种可以有如下操作:
1 向x中灌满水
2 向y中灌满水
3 向x中倒完水
4 向y中倒完水
5 把x的水倒向y里，直到装满或者倒空
6 把y的水倒向x里，直到装满或者倒空
那么可以用，remain_x remain_y 来表示x和y里水的总量。用栈来模拟dfs的递归操作，用seen来存放所有已经检查过的情况
时间复杂度：O（xy） 
空间复杂度: O(xy)
'''

class Solution:
    def canMeasureWater(self, x, y, z):
        if x + y < z: return False
        if x == 0 or y == 0:
            return z == 0 or x + y == z
        return z % math.gcd(x, y) == 0


        # seen = set()
        # stack = [(0, 0)]
        # while stack:
        #     remain_x, remain_y = stack.pop()
        #     if remain_x == z or remain_y == z or remain_x + remain_y == z:
        #         return True
        #     if (remain_x, remain_y) in seen:
        #         continue
        #     seen.add((remain_x, remain_y))
        #     stack.append((remain_x, y))     # y中倒满水
        #     stack.append((x, remain_y))     # x中到满水
        #     stack.append((0, remain_y))    # x倒空水
        #     stack.append((remain_x, 0))    # y倒空水
        #     # 解释一下两部，因为一个壶的水倒进另一个壶里的终止条件为 倒满或者倒空，我们用 min（）来判断 被倒的壶中空的量和倒的壶水的余量谁更少
        #     # 如果 倒的壶中的水为 1，被倒的壶中空的水量为 2，当水倒完后，被倒的壶肯定没有装满
        #     stack.append((remain_x - min(remain_x, y - remain_y), remain_y + min(remain_x, y - remain_y)))  # x倒进y里，直到倒满或者倒空
        #     stack.append((remain_x + min(remain_y, x - remain_x), remain_y - min(remain_y, x - remain_x)))  # y倒进x里，直到倒满或者倒空
        return False

if __name__ == '__main__':
    x, y, z = 3, 5, 4
    out = Solution().canMeasureWater(x, y, z)
    print(out)