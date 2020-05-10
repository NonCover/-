"""
author: noc
time: 2020年5月10日
url: https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""
递归法：我们要找节点p，q的公共组先，并且这个公共祖先要求的深度最大，那么我们可以假设当前root为p，q的公共祖先，然后判断root的左子树或者右子树存不存在p和q，
如果root = p的时候，说明q在p的左子树或者右子树中，如果root = q时，说明p在q的左子树或右子树中
那么递归解析就可以得出：
    1. 递归出口： 当root等于 None， 或者等于p或者q得时候，直接返回root
    2. 递归工作：在根节点的左子树进行查找p或q，在根节点的右子树进行查找工作
    3. 返回值：如果左子树中递归到 None 时，说明p，q节点在右子树中，直接返回right
              如果右子树为空时，说明，p，q系欸但在左子树中，直接返回left
              否则说明，p，q节点分别在不同的子树，此时返回root
"""
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root == None or p == root or q == root: return root      ## 递归基
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left == None: return right
        if right == None: return left
        return root

from typing import List
def arr2Tree(arr: List):
    root = TreeNode(arr[0])
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(arr):
        node = nodeQueue[front]
        item = arr[index]
        index += 1
        if item:
            node.left = TreeNode(item)
            nodeQueue.append(node.left)
            if index >= len(arr): break
        item = arr[index]
        index += 1
        if item:
            node.right = TreeNode(item)
            nodeQueue.append(node.right)
            if index >= len(arr): break
        front += 1
    return nodeQueue

if __name__ == '__main__':
    arr = [3,5,1,6,2,0,8,None,None,7,4]
    nodes = arr2Tree(arr)
    root = nodes[0]
    p, q = nodes[5], nodes[6]
    out = Solution().lowestCommonAncestor(root, p, q)
    print(out.val)