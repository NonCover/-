"""
author: noc
time: 2020年5月22日
url: https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        import collections
        idxMap = collections.defaultdict();
        def myBuildTree(preorder_left, preorder_right, inorder_left, inorder_right):
            if preorder_left > preorder_right: return None
            root = TreeNode(preorder[preorder_left])
            idx = idxMap[preorder[preorder_left]]
            root.left = myBuildTree(preorder_left + 1, preorder_left + idx - inorder_left, inorder_left, idx - 1)
            root.right = myBuildTree(preorder_left + idx - inorder_left + 1, preorder_right, idx + 1, inorder_right)
            return root
        for i in range(len(inorder)):
            idxMap[inorder[i]] = i
        return myBuildTree(0, len(preorder) - 1, 0, len(inorder) - 1)

