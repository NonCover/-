'''
author:noc
time:2020年4月10日
url:https://leetcode-cn.com/problems/balanced-binary-tree/
'''
'''
自定向上的回溯。我们先判断二叉树的每个左子树 右子树是否为平衡二叉树，是的话，我们返回它的长度还要 加 1，再来判断父节点是否为平衡二叉树。如果不为二叉树的话直接返回-1
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root):
        return self.recur(root) != -1

    def recur(self, root):
        if not root: return 0
        left = self.recur(root.left)
        if left == -1: return -1
        right = self.recur(root.right)
        if right == -1: return -1
        return max(left, right) + 1 if abs(left - right) < 2 else -1

def arr2tree(inputValues):
    root = TreeNode(inputValues[0]) # 根节点
    nodeQueue = [root]  # 保存节点的队列
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1
        item = inputValues[index]
        index = index + 1
        if item != None:
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)
            if index >= len(inputValues):
                break
        item = inputValues[index]
        index = index + 1
        if item != None:
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


if __name__ == '__main__':
    root = arr2tree([1,2,2,3,None,None,3,4,None, None,4])
    out = Solution().isBalanced(root)
    print(out)