'''
author: noc
time: 2020年4月12日
url：https://leetcode-cn.com/problems/intersection-lcci/
'''
'''
这是一道几何体，如果是做游戏开发以及图像处理需要了解。
两个线段如果不相交必然满足以下某个条件：
1. 斜率 K 相同（平行）：
    1.截距b不相等
    2.截距b相等，线段的两个顶点不出现在另一个线段中
2. 斜率 K 不同（不平行）：
    1.线段的两个顶点不出现在另一个线段中
总之，此题不是人做的。大量的逻辑判断，需要不是人的几何知识，虽然放在现实中一眼就能看出，可计算机不是人。
时间复杂度：O（1）  # 线性计算
空间复杂度：O（1）  
'''

class Solution:
    def intersection(self, start1, end1, start2, end2):
        k1 = (end1[1] - start1[1]) / (end1[0] - start1[0]) if (end1[0] - start1[0]) else None
        b1 = start1[1] - k1 * start1[0] if k1 is not None else None
        k2 = (end2[1] - start2[1]) / (end2[0] - start2[0]) if (end2[0] - start2[0]) else None
        b2 = start2[1] - k2 * start2[0] if k2 is not None else None

        if k1 is None and k2 is None:  # 两条都是垂线
            if start1[0] == start2[0] and min(start1[1], end1[1]) <= max(start2[1], end2[1]) and min(start2[1],
                                                                                                     end2[1]) <= max(
                    start1[1], end1[1]):
                # 仅当X相同、直线1的底端小于直线2的顶端、直线2的底端小于直线1的顶端时，才有交点，
                # 且最小的交点是两直线底端的较大者，如果要最大的交点就是直线顶端的较小者
                return max(min(start1, end1), min(start2, end2))
        elif k1 is None:  # 直线1是垂线，直线2不是
            y = k2 * start1[0] + b2
            if (start2[1] - y) * (end2[1] - y) <= 0:
                return [start1[0], y]
        elif k2 is None:  # 直线2是垂线，直线1不是
            y = k1 * start2[0] + b1
            if (start1[1] - y) * (end1[1] - y) <= 0:
                return [start2[0], y]
        else:  # 都不是垂线
            if k1 == k2 and b1 == b2 and min(start1[1], end1[1]) <= max(start2[1], end2[1]) and min(start2[1],
                                                                                                    end2[1]) <= max(
                    start1[1], end1[1]):  # 两线斜率相同、截距相同，类似两条垂线时的判断
                return [max(min(start1[0], end1[0]), min(start2[0], end2[0])),
                        max(min(start1[1], end1[1]), min(start2[1], end2[1]))]
            elif k1 != k2:  # 两线斜率不同
                x = (b2 - b1) / (k1 - k2)
                y = k1 * x + b1
                if (start2[1] - y) * (end2[1] - y) <= 0 and (start1[1] - y) * (end1[1] - y) <= 0:
                    return [x, y]
        return []


if __name__ == '__main__':
    start1 = [0,0]
    end1 = [1, 1]
    start2 = [2, 2]
    end2 = [3, 3]
    out = Solution().intersection(start1, end1, start2, end2)
    print(out)
