'''
@author:noc
@time:2020年3月23日
@url:https://leetcode-cn.com/problems/middle-of-the-linked-list/
'''

class ListNode:
    def __init__(self, x = None):
        self.val = x
        self.next = None

'''
解法1：利用快慢指针遍历链表，每次移动一次慢指针，就移动两次快指针，这样的话，每次慢指针都在中间位置，直到快指针移动到tail时，就返回慢指针。
时间复杂度：O（N）取决于链表的长度
空间复杂度：O（1）两个指针指向的节点
解法2：进行一次遍历链表，将节点保存到数组里，然后返回 数组中间值
时间复杂度：O（N）
空间复杂度：O（N）
'''
class Solution:
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

def arr2List(arr):
    head = ListNode()
    node = ListNode()
    for i in arr:
        if not head.val:
            node = ListNode(i)
            head = node
        else:
            node.next = ListNode(i)
            node = node.next
    return head

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 4, 5]
    head = arr2List(arr)
    out = Solution().middleNode(head)
    print(out.val)