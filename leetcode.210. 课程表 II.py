"""
author: noc
time: 2020年5月17日
url: https://leetcode-cn.com/problems/course-schedule-ii/
"""

"""
拓扑排序：
首相将课程数组转换成一个有向图，可以用集合类中的字典实现，然后我们需要一个数组in_degree来存放每一个课程的入度，也就是某个课程有多少的课程指向
它，如果该课程的入度为0的话，说明该课程是第一个学习的课程，加入队列中进行递归，每次队列出队就加入答案数组，然后再从有向图中找该课程指向了那些课程，
然后将该课程的入度减一，如果减到0的话，就把该课程入队。知到队列为空退出递归。
"""

import collections
class Solution:
    from typing import List
    def fingOrder(self, numCourse: int, prerequisites: List[List[int]]) -> List[int]:
        edeges = collections.defaultdict(list)      ## 有向图
        in_degree = [0] * numCourse                 ## 入度
        ans = []                                    ## 答案
        for course in prerequisites:
            in_degree[course[0]] += 1
            edeges[course[1]].append(course[0])
        queue = [i for i in range(numCourse) if in_degree[i] == 0]
        while queue:
            c = queue.pop(0)
            ans.append(c)
            for x in edeges[c]:
                in_degree[x] -= 1
                if in_degree[x] == 0:
                    queue.append(x)

        return ans if len(ans) == numCourse else []

if __name__ == '__main__':
    prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    numCourse = 4
    out = Solution().fingOrder(numCourse, prerequisites)
    print(out)