'''
@author: noc
@time：2020年3月17日
@url：https://leetcode-cn.com/problems/find-words-that-can-be-formed-by-characters/
'''
import collections
'''
题解：统计每个词在单词出现的次数，然后于chars中出现的次数进行比较，大于的话，则表示，无法满足每个字母仅使用一次的情况下还能够拼出单词
'''
class Solution(object):
    def countCharacters(self, words, chars):
        ret = 0
        chars_cnt = collections.Counter(chars)
        for word in words:
            for w in word:
                if word.count(w) > chars_cnt[w]:
                    break
            else:
                ret += len(word)
        return ret

if __name__ == '__main__':
    words = ["hello","world","leetcode"]
    chars = "welldonehoneyr"
    out = Solution().countCharacters(words, chars)
    print(out)