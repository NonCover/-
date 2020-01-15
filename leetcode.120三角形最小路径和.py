# -*- coding:utf-8 -*-
#__author__ = noc#
#2.三角形最小路径和#
##描述:
# 给定一个三角形，找出自顶向下的最小路径和。
# 每一步只能移动到下一行中相邻的结点上。##
class solution(object):
    def Path(self, Triangle):
        if not Triangle: return 0
        n = len(Triangle)
        Min4Line = min(Triangle[n-1][i] for i in range(n-1))
        PathValue = [] 
        for i in range(n-2, -1, -1):
            for j in range(i+1):
                Triangle[n-1][j] = min(Triangle[n-1][j], Triangle[n-1][j+1]) + Triangle[i][j]
            MinValue = min(Triangle[n-1][k] for k in range(j+1))      
            for L in range(len(Triangle[j+1])):     #判断返回上一个的值的索引
                if Triangle[n-1][L] is MinValue:
                    PathValue.append(str(Triangle[i][L]))
                    break
        #print(PathValue)
        print('路径：')
        for i in range(n-2, -1, -1):
            print(PathValue[i], end = '->')
        print(Min4Line)
        print('路径最小和:')
        return Triangle[n-1][0]
if __name__ == '__main__':
    Tri = [[1],[0,4],[4,1,3],[5,5,9,6]]
    s = solution()
    print(s.Path(Tri))
