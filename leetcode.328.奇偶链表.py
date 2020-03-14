'''
@author：noc
@time：2020年3月14日
@url：https://leetcode-cn.com/problems/odd-even-linked-list/
'''

class ListNode(object):
    def __init__(self, x = None):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        # 用 even_head指向 偶位的头，even指向下一个偶位 odd将奇位的下一个指向奇位
        odd = head
        even = head.next
        even_head = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head

def arr2list(arr):
    node = ListNode()
    head = ListNode()

    for a in arr:
        if not node.val:
            node = ListNode(a)
            head = node
        else:
            node.next = ListNode(a)
            node = node.next
    return head

def prt_list(head):
    while head:
        print(head.val)
        head = head.next

if __name__ == '__main__':
    head = arr2list([1, 2, 3, 4, 5, 6])
    out = Solution().oddEvenList(head)
    prt_list(out)
