"""
author: noc
time: 2020年6月10日
url: https://leetcode-cn.com/problems/palindrome-linked-list/
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


from typing import List
def arr2List(arr: List):
    head = ListNode(-1)
    head.next = ListNode(arr.pop(0))
    p = head.next
    while arr:
        p.next = ListNode(arr.pop(0))
        p = p.next
    return head.next

"""
题解：
    
"""

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head == None or head.next == None:
            return True
        p = ListNode(-1)
        p.next = head
        slow, fast = p, p
        ## 找到链表中间节点
        while fast != None and fast.next != None:
            slow, fast = slow.next, fast.next.next

        ## 从中间节点断开，将后半段置反
        prev, curr = None, slow.next
        slow.next = None    ## 断开
        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        ## 开始比较两段，注意不要写成 head != None, 因为链表为偶数，前半段比后半段多一个值
        while prev != None:
            if prev.val != head.val: return False
            prev, head = prev.next, head.next
        return True

if __name__ == '__main__':
    arr = [1, 2, 1]
    head = arr2List(arr)
    out = Solution().isPalindrome(head)
    print(out)