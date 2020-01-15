#!/usr/bin/env python
#-*- coding:utf-8 -*-
#__author__ = noc
#6.打开转盘锁 Lang:python
##描述:
# 利用BFS算法进行最短路径求解##

from queue import Queue

class solution:
    def openlock(self, deadends, target):
        deadends = set(deadends)    #使重复的删除
        if '0000' in deadends:
            return -1
        q = Queue()     #创建一个队列
        q.put(('0000', 0))
        res = '0000'
        while not q.empty():
            node, step = q.get()
            for i in range(4):
                for add in (1, -1):
                    res = node[:i] + str((int(node[i]) + add) % 10) + node[i+1:]
                    if not res in deadends:  
                        q.put((res, step + 1))
                        deadends.add(res)
                    if res == target:
                        return step+1
        return -1
if __name__ == '__main__':
    deadends = ["0201","0101","0102","1212","2002"]
    target = "3030"
    print('一共需要转动:',solution.openlock(solution, deadends, target), '次')