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
class Root:
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

if __name__ == "__main__":
    tree = Root(1, Root(2, Root(3), Root(4)), Root(2, Root(4), Root(3)))
    # 二叉树创建
    print(Solution1(tree))
    print(Solution2(tree))