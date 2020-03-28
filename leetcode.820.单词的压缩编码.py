'''
@author：noc
@time：2020年3月28日
@url：https://leetcode-cn.com/problems/short-encoding-of-words/
'''
'''
题解：利用集合去重，然后再遍历数组，words[i]代表第i个单词，我们再从这个单词里找到一个存在于集合里的单词 words[i][j for j in range(1, len(words[i])):] ,将这个单词删除掉，因为我们的目的是要得到最小编码长度，
例如：time，它包含的单词有，ime，me，e。我们就可以从集合中删除掉这几个单词。再在time后面加上结束符 ‘#’
'''

class Solution:
    def minimumLengthEncoding(self, words):
        good = set(words)
        for word in words:
            for j in range(1, len(word)):
                good.discard(word[j:])
        return sum(len(v) + 1 for v in good)

if __name__ == '__main__':
    words = ["me", "time"]
    out = Solution().minimumLengthEncoding(words)
    print(out)