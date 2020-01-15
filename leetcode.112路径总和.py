#!/usr/bin/env python
#-*- coding:utf-8 -*-
#__author__ = noc
#4.计算二叉树的路径总和，并判断与给定的值是否相等，相等返回Fals，否则返回True   Lang：python

#创建一个二叉树
class TreeNode(object):
    def __init__(self, val = None, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root, sum):
        if not root:
            return False
        sum -= root.val
        if not root.left and not root.right:
            return sum == 0
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
#像二叉树中插入值:
def insert(root, val):   
    if root is None:
        root = TreeNode(val)
    else:
        if val < root.val:
            root.left = insert(root.left, val)
        elif val > root.val:
            root.right = insert(root.right, val)
    return root
if __name__ == '__main__':
    root = TreeNode(5, TreeNode(3, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(10), TreeNode(4, TreeNode(None), TreeNode(1))))    
    #root = TreeNode([5,3,8,11,None,10,4,7,2,None,None,None,1])
    res = Solution.hasPathSum(Solution(), root, 21)
    print(res)
