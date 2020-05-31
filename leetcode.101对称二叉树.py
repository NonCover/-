#@Author = noc @level = 容易
'''
给定一个二叉树，检查它是否是镜像对称的。
例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
    1
   / \
  2   2
   \   \
   3    3
说明:
如果你可以运用递归和迭代两种方法解决这个问题，会很加分。
'''
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.x = x
        self.left = left
        self.right = right

def Solution1(root):
    '''递归法求解'''
    # 数为空直接返回True
    if not root: return True
    def s(left, right):
        if not (left or right):
            # 节点都为空时，树遍历完成
            return True
        if not (left and right):
            # 比较的两个节点只有一个存在
            return False
        if left.x != right.x:
            return False
        return s(left.left, right.right) and s(left.right, right.left)
    return s(root.left, root.right)

def Solution2(root):
    '''迭代法求解'''
    if not root: return True
    queue = []
    queue.append(root.left)
    queue.append(root.right)
    while queue:
        right = queue.pop()
        left = queue.pop()
        if right == None and left == None: continue     # 当前节点都为空
        if right == None or left == None: return False  # 节点不都为空
        if right.x != left.x: return False              # 节点值不行等
        queue.append(left.left)
        queue.append(right.right)
        queue.append(left.right)
        queue.append(right.left)
        # print(queue)
    return True

from typing import List
def arr2tree(arr: List) -> TreeNode:
    head = TreeNode(arr[0])
    node_arr = [head]
    node = head
    front = 0
    idx = 1
    while idx < len(arr):
        node = node_arr[front]
        front += 1
        item = arr[idx]
        idx += 1
        if item:
            node.left = TreeNode(item)
            node_arr.append(node.left)
            if idx == len(arr):
                break
        item = arr[idx]
        idx += 1
        if item:
            node.right = TreeNode(item)
            node_arr.append(node.right)
            if idx == len(arr):
                break
    return head

if __name__ == "__main__":
    tree = arr2tree([1,2,2,3,4,4,3])
    # 二叉树创建
    print(Solution1(tree))
    print(Solution2(tree))