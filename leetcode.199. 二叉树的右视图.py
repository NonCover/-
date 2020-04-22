'''
author: noc
time: 2020年4月22日
url: https://leetcode-cn.com/problems/binary-tree-right-side-view/
'''
'''
两种解法：
1. DFS：
    我们照样递归法来解DFS类型的问题，首先需要明确的是我们是保存右视图看到的节点，所以我们一开始对右子树进行深搜，直到搜到底，在回溯，去搜左子树继续搜到底，那么我们需要注意一点，也就是深度问题，
    如果右子树的深度在整个二叉树是最深的，那么其他树就无法被观察到，我们需要用一个变量来保存最深的子树的深度，然后我们再用一个变量来存放每个节点的深度，如果节点的深度大于历史最长深度的话，那么这个节点
    就可以被观察到，更新最长深度为当前节点的深度
2. BFS：
    这道题其实BFS是最容易理解，也是最容易想出来的，我们每次搜每一层的节点，保存起来，只需要把每一层的节点最后一个保存进答案数组即可

时间/空间复杂度：O（N）
'''

from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
DFS
'''
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: return []
        ans = [root.val]
        self.depth = 0
        def dfs(node, d):
            if not node:
                self.depth = max(self.depth, d - 1)
                return
            if d > self.depth:
                ans.append(node.val)
            dfs(node.right, d + 1)
            dfs(node.left, d + 1)
        dfs(root.right, 2)
        dfs(root.left, 2)
        return ans
'''
BFS
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: return []
        ans = []
        lvl = [root]
        while lvl:
            ans.append(lvl[-1].val)
            q, lvl = lvl, []
            while q:
                node = q.pop(0)
                if node.left: lvl.append(node.left)
                if node.right: lvl.append(node.right)
        return ans
'''
def arr2tree(inputValues):
    if not inputValues: return None
    root = TreeNode(inputValues[0])  # 根节点
    nodeQueue = [root]  # 保存节点的队列
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1
        item = inputValues[index]
        index = index + 1
        if item != None:
            leftNumber = item
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)
            if index >= len(inputValues):
                break
        item = inputValues[index]
        index = index + 1
        if item != None:
            rightNumber = item
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root

if __name__ == '__main__':
    node = [1,2,3,None,5,6,4,None,6,7]
    root = arr2tree(node)
    out = Solution().rightSideView(root)
    print(out)