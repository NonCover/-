'''
author: noc
time: 2020年4月14日
url: https://leetcode-cn.com/problems/add-two-numbers-ii/
'''
'''
由于做加法从低位到高位会进位，所以我们将连个链表分别压入到两个栈中，然后同时出栈加法，再把值加到新链表中。

'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        s1 = []
        s2 = []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        ans = None
        carry = 0
        while s1 or s2 or carry:
            a = 0 if not s1 else s1.pop()
            b = 0 if not s2 else s2.pop()
            curr = a + b + carry
            carry = curr // 10
            curr %= 10
            currNode = ListNode(curr)
            currNode.next = ans
            ans = currNode

        return ans

def arr2list(arr):
    root = ListNode(-1)
    node = root
    for i in arr:
        node.next = ListNode(i)
        node = node.next
    return root.next

def printList(head):
    while head:
        print(head.val, end='->')
        head = head.next
    print("None")

if __name__ == '__main__':
    arr1 = [7,2,4,3]
    arr2 = [5,6,4]
    l1 = arr2list(arr1)
    l2 = arr2list(arr2)
    out = Solution().addTwoNumbers(l1, l2)
    printList(out)