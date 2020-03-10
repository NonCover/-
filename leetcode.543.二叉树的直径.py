'''
@author: noc
@time: 2020年3月10日
@url: https://leetcode-cn.com/problems/diameter-of-binary-tree/
'''

class TreeNode(object):
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def diameterOfBinaryTree(self, root):
        # 返回二叉树中，两个节点之间的路径最长
        self.ret = 0    # 保存当前最大的路径

        def depath(node):
            if not node: return 0   # 为空，返回 0 
            
            L = depath(node.left)   # 递归，找到左儿子的最长路径
            R = depath(node.right)  # 找到该节点的右子树的最长路径

            self.ret = max(self.ret, L + R + 1) # 最长路径是 左子树的最长加上右子树的最长
            return max(L, R) + 1    # 返回该节点下的

        depath(root)
        return self.ret - 1

def mid(node):
    if not node: return
    mid(node.left)
    print(node.val)
    mid(node.right)

if __name__ == "__main__":
    root = TreeNode(1, 
                        TreeNode(2, 
                            TreeNode(4), 
                            TreeNode(5)), 
                        TreeNode(3))
    out = Solution().diameterOfBinaryTree(root)
    print(out)