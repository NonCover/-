'''
@author:noc
@timr:2020年4月10日
@url:https://leetcode-cn.com/problems/reverse-words-in-a-string/
'''
'''
思路：先将s两边的空格去掉，然后再创建一个双端队列和一个字符。双端队列来保存最终结果，字符来保存每一次的单词，因为双端队列可以支持再对头插入元素
'''
from collections import deque

class Solution:
    def reverseWords(self, s):
        '''
        调用函数
        return ' '.join(s.split()[::-1])
        '''
        left, right = 0, len(s) - 1
        while left < right and s[left] == ' ':
            left += 1
        while right > left and s[right] == ' ':
            right -= 1
        ret, word = deque(), ''
        while left <= right:
            if s[left] == ' ' and word:
                ret.appendleft(word)
                word = ''
            elif s[left] != ' ':
                word += s[left]
            left += 1
        ret.appendleft(word)    # 最后一个单词无法加入到结果中
        print(' '.join(ret))

if __name__ == '__main__':
    s = "the sky is blue"
    Solution().reverseWords(s)
