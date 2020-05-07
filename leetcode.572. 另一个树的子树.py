"""
author: noc
time: 2020年5月7日
url: https://leetcode-cn.com/problems/subtree-of-another-tree/
"""
"""
递归法: 搜索二叉树的每一个节点，判断这个节点的子树是否为t树，如果不是继续向下搜索s。详情见代码
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not t: return True   ## t为空
        if not s: return False  ## s为空，此时t不可能为空
        ## 如果s当前节点的子树不为t，就分别递归s的左子树和右子树来判断
        return self.isSama(s, t) or \
               self.isSubtree(s.right, t) or \
               self.isSubtree(s.left, t)


    def isSama(self, s: TreeNode, t: TreeNode) -> bool:
        ## 两节点为空
        if not (s and t): return True
        ## 某个节点为空
        if not (s or t): return False
        ## 两节点值不相等
        if (s.val != t.val): return False
        ## 说明当前s，t对应节点相等，继续向下判断
        return self.isSama(s.left, t.left) and self.isSama(s.right, t.right)

def arr2Tree(inputValue):
    root = TreeNode(inputValue[0])
    nodeArray = [root]
    front = 0
    index = 1
    while index < len(inputValue):
        item = inputValue[index]
        node = nodeArray[front]
        front += 1
        index += 1
        if item:
            node.left = TreeNode(item)
            nodeArray.append(node.left)
        item = inputValue[index]
        index += 1
        if item:
            node.right = TreeNode(item)
            nodeArray.append(node.right)
    return root


if __name__ == '__main__':
    s = [3,4,5,1,2]
    t = [4,1,2]
    s = arr2Tree(s)
    t = arr2Tree(t)
    out = Solution().isSubtree(s, t)
    print(out)