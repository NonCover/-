#@author=noc @level=容易
'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
示例 1:
输入: "()"
输出: true
示例 2:
输入: "()[]{}"
输出: true
示例 3:
输入: "(]"
输出: false
示例 4:
输入: "([)]"
输出: false
示例 5:
输入: "{[]}"
输出: true
'''
def isValid(s):
    stack = []
    mapping = {')':'(', '}':'{', ']':'['}
    for i in s:
        if i in mapping:
            top_element = stack.pop() if stack else '#'
            if top_element != mapping[i]:
                return False
        else:
            stack.append(i)
    return not stack

print(isValid('{}{()}'))
