'''
author: noc
time: 2020年4月26日
url: https://leetcode-cn.com/problems/merge-k-sorted-lists/
'''
"""
采用分治思想，把K个链表分支撑 K/2个链表 K/4个链表， 直到分支撑两个链表后，开始合并，合并时进行判断，满足递增链表，最后再合成一个新的链表
"""
import heapq
from typing import List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        N = len(lists)
        if N == 1: return lists[0]
        if N == 0: return None
        return self.merge(lists, 0, N - 1)

    def merge(self, lists, left, right):
        if left == right: return lists[left]
        mid = left + (right - left) // 2
        l1 = self.merge(lists, mid + 1, right)
        l2 = self.merge(lists, left, mid)
        return self.mergeList(l1, l2)

    def mergeList(self, l1, l2):
        if not l1: return l2
        if not l2: return l1
        if l1.val <= l2.val:
            l1.next = self.mergeList(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeList(l1, l2.next)
            return l2

def arr2list(arr):
    ans = []
    for a in arr:
        root = ListNode(-1)
        node = root
        for v in a:
            node.next = ListNode(v)
            node = node.next
        ans.append(root.next)
    return ans

if __name__ == '__main__':
    arr = [[1, 3, 5],
           [2, 4, 7],
           [4, 5, 7]]
    lists = arr2list(arr)
    out = Solution().mergeKLists(lists)
