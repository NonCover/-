# @author: noc
# @time: 2020年3月2日17点12分
# @url: https://leetcode-cn.com/problems/reverse-linked-list/
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 反转链表
    def reverseList(self, head: ListNode) -> ListNode:
        # prev = None
        # curr = head
        # while curr != None:
        #     nextNode = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = nextNode
        # return prev
        prev = None
        while head:
            nextNode = head.next
            curr = head
            curr.next = prev
            prev = curr
            head = nextNode
        return curr

if __name__ == "__main__":
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    ret = Solution().reverseList(l1)
    while ret:
        print(ret.val, end=' ')
        ret = ret.next