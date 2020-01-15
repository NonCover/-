# -*- coding: utf-8 -*-
#__author__ = noc#
#1.回合制手表 Long = python#

def readbase2Wacth(num):
    res = []
    for i in range(12):
        for j in range(60):
            if num == bin(i).count('1') + bin(j).count('1'):
                res.append('%d:%02d'%(i, j))
    return res
def main(num):
    return readbase2Wacth(num)
num = input()
print(main(int(num)))