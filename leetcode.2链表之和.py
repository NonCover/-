#!/usr/bin/python
#-*- coding:utf-8 -*-
#__author__ = noc
#2.
'''
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807  
'''
class ListNode(object):
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
    def __str__(self):
        return str(self.val)

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        new = ListNode(0)
        last = new
        while l1 or l2:
            value = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry, value = value // 10, value % 10
            last.next = ListNode(value)
            last = last.next
            l1, l2 = l1.next if l1 else None, l2.next if l2 else None
        if carry:
            last.next = ListNode(carry)
        return self.printNode(new.next)

    def printNode(self, node):
        while node:
            if node.next is None:
                print(node)
            else:
                print(node, end='->')
            node = node.next

def generateList(l: list) -> ListNode:
    prenode = ListNode(0)
    lastnode = prenode
    for val in l:
        lastnode.next = ListNode(val)
        lastnode = lastnode.next
    return prenode.next

if __name__ == "__main__":
    l1 = generateList([1,2,5,6])
    l2 = generateList([3,6,4])
    s = Solution()
    s.addTwoNumbers(l1, l2)
