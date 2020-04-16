'''
作者：noc
日期：2020年4月16日
url：https://leetcode-cn.com/problems/merge-intervals/
'''
'''
本质思想是排序。先把每个区间的开始位置从小到大进行排序，然后比较每个区间右端的位置，如果下一个区间开始位置当前区间的结束为止，说明两个区间不相交。
反之，就要判断两个区间的结束为止谁大。

总而言之，几种排序方式要学好，归并 快排 堆排 插入 这儿我们就调用函数了。本理解本质思想即可
'''
class Solution:
    def merge(self, intervals):
        if not intervals or len(intervals[0]) == 0: return intervals
        intervals.sort(key=lambda x: x[0])
        # print(intervals)
        ans = []
        for interval in intervals:
            if not ans or ans[-1][1] < interval[0]:
                ans.append(interval)
            else:
                ans[-1][1] = max(ans[-1][1], interval[1])
        return ans
if __name__ == '__main__':
    intervals = [[1,3],[8, 10],[2, 6],[15,18]]
    out = Solution().merge(intervals)
    print(out)