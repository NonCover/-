"""
author: noc
time: 2020年5月16日
url: https://leetcode-cn.com/problems/reverse-nodes-in-k-group/
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

"""
解析：题目不复杂，主要考查代码的设计能力
首先，我们需要反转k个节点，我们需要两个指针head和tail，这两个指针分别指向k个连续节点的头部和尾部，
然后我们在对其进行反转（关于链表的反转参考206），此时我们返回新链表的head和tail，然后我们就要把这个新的链表
重新接入到整个链表当中。
"""
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        hair = ListNode(-1)     # 此链表头用来保存新链表的
        hair.next = head
        pre = hair  # 保存head的上一个节点
        while head:
            tail = pre
            for _ in range(k):
                tail = tail.next
                if not tail:
                    return hair.next
            nextNode = tail.next    # 存放tail的下一个节点
            head, tail = self.reverse(head, tail)   ## 得到新的链表头和尾
            ## 将得到的新链表接入到整体中
            pre.next = head
            tail.next = nextNode

            pre = tail
            head = tail.next
        return hair.next

    def reverse(self, head, tail):
        pre = tail.next
        p = head
        while pre != tail:
            nextNode = p.next
            p.next = pre
            pre = p
            p = nextNode
        return tail, head

from typing import List
def arr2listNode(arr) -> ListNode:
    root = ListNode(arr[0])
    node = root
    for i in range(1, len(arr)):
        node.next = ListNode(arr[i])
        node = node.next
    return root

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    root = arr2listNode(arr)
    out = Solution().reverseKGroup(root, 2)
    while out:
        print(out.val)
        out = out.next