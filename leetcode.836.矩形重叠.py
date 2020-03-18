'''
@author：noc
@time：2020年3月18日
@url：https://leetcode-cn.com/problems/rectangle-overlap/
'''
'''
解法：一开始我想到了几种情况，也就是两个矩阵在坐标系中所在的位置，后来越想越觉得可能性太多了，要考虑的条件太多，后来转眼一想，可以分别把两个矩阵分别投影到x和y轴上，
但是问题又来了，那么又该如何判断两个矩阵是否重叠呢，rec1投影到x轴上的线段也就是 (a1, a2) rec2 -》 (b1, b2)， y轴同理，那么重叠的条件也就是： b1 < a2 < b2,
y轴同理，如果满足条件的话，就可以返回True了，也就是需要判断四次 基于两个矩阵的相对位置，代码写了下来后，觉得还是太复杂，看了题解后，深深的觉得自己的智商太低了，
为何我不判断两个矩阵不重叠，然而不重叠的条件更加简单，也就是 a2 < b1（y轴同理），当然一条平行于x轴的线段，一条线段的最右边小于另一条线段的最左边，那么这两条线段肯定没有公共区域。
>>>我太蠢了<<<
时间复杂度O(1)   
'''
class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        is_X = not (rec1[2] <= rec2[0] or rec1[0] >= rec2[2])
        is_Y = not (rec1[3] <= rec2[1] or rec1[1] >= rec2[3])
        return is_X and is_Y

if __name__ == '__main__':
    rec1 = [0, 0, 2, 2]
    rec2 = [1, 1, 3, 3]
    out = Solution().isRectangleOverlap(rec1, rec2)
    print(out)