#@Author = noc @level = 容易
'''
你需要采用前序遍历的方式，将一个二叉树转换成一个由括号和整数组成的字符串。
空节点则用一对空括号 "()" 表示。而且你需要省略所有不影响字符串与原始二叉树之间的一对一映射关系的空括号对。
示例 1:
输入: 二叉树: [1,2,3,4]
       1
     /   \
    2     3
   /    
  4     
输出: "1(2(4))(3)"
解释: 原本将是“1(2(4)())(3())”，
在你省略所有不必要的空括号对之后，
它将是“1(2(4))(3)”。
示例 2:
输入: 二叉树: [1,2,3,null,4]
       1
     /   \
    2     3
     \  
      4 
输出: "1(2()(4))(3)"
解释: 和第一个示例相似，
除了我们不能省略第一个对括号来中断输入和输出之间的一对一映射关系。
'''
class Root:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

def Solution(t):
    if not t: return ''
    stack = []
    looked = set()
    ans = ''
    stack.append(t) # 入栈
    while stack:
        v = stack[-1]
        if v in looked:     # 如果该节点被检查过，出栈，并且闭合一个括号
            stack.pop()
            ans += ')'
        else:
            looked.add(v)
            if v.left and v.right:
                stack.append(v.right)
                stack.append(v.left)
                ans += ('(' + str(v.val))
            if v.left and v.right == None: 
                stack.append(v.left)
                ans += ('(' + str(v.val))
            if v.left == None and v.right:
                stack.append(v.right)
                ans += ('(' + str(v.val) + '()') 
            if v.left == None and v.right == None:
                ans += ('(' + str(v.val))   
    ans = ans[1:len(ans)-1]     # 去掉两边的括号
    return ans

if __name__ == "__main__":
    tree = Root(1,Root(1), Root(1))
    print(Solution(tree))