"""
@author: noc
@time: 2020年6月18日
@url: https://leetcode-cn.com/problems/recover-a-tree-from-preorder-traversal/
"""

"""
解法：
    利用栈来模拟构建二叉树，首先根据题意，多少个‘-’代表，后面所对应的数字的深度，也就是二叉树在那一层的层级，注意的是二叉树的根节点的深度为 0
    由于先序遍历是按照 根 左 右 的顺序来便利的，所以我们用栈来模拟。要注意栈的高度就是栈顶元素的深度，至于为什么是？
    跟着思路在纸上演算几遍就理解了。
    如果我们某一元素的深度与栈高相等，直接将该节点插入到栈顶元素的左子树，然后该节点入栈。
    如果不相等，就需要依次出栈，直到栈高与该节点的深度相等，此时我们插入到栈顶的右子树钟，此时他的左子树已经被弹出，也就是栈顶的左子树已经存在了。
    
    总结思路：
        1.遍历字符串，记录每个数字的深度
        2.比较栈高与深度是否相等
            相等，直接与栈顶的左子树连接，并入栈
            不等，出栈直到栈高与深度相等为止，然后与右子树相连接。并入栈
        3.返回栈底即可
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        path = []   # 存放节点的栈
        n = len(S)
        pos, cnt = 0, 0
        while pos < n:
            level = 0

            while S[pos] == '-':    ## 计算出当前节点的层级
                level += 1
                pos += 1
            val = 0
            while pos < n and S[pos] != '-':    ## 当前节点的值
                val = val * 10 + int(S[pos])
                pos += 1

            node = TreeNode(val)

            if cnt == level:    ## 栈的元素与当前节点的层级相等，插入到左子树
                if cnt != 0:
                    path[cnt - 1].left = node
                path.append(node)
                cnt += 1

            else:
                while cnt > 1 and cnt != level:
                    path.pop(-1)
                    cnt -= 1
                path[cnt - 1].right = node
                path.append(node)
                cnt += 1
        return path[0]



if __name__ == '__main__':
    S = "1-2--3--4-5--6--7"
    out = Solution().recoverFromPreorder(S)
    print(out.val)
