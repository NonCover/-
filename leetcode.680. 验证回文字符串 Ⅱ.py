"""
author: noc
time: 2020年5月19日
url: https://leetcode-cn.com/problems/valid-palindrome-ii/
"""

"""
双指针：两个指针分别从字符串的两端向中间缩小范围，如果两个字符不相等的话，需要删除某个字符有两种情况，
s[l] != s[r]，可能回文字符是闭区间[l + 1, r]或者[l, r - 1]，所以两个区间检查一下.
"""

class Solution(object):
    def validPalindrome(self, s: str) -> bool:
        size = len(s)
        left, right = 0, size - 1
        while left < right:
            if (s[left] != s[right]):
                return self._valid(s, left + 1, right) or self._valid(s, left, right - 1)
            else:
                left += 1
                right -= 1
        return True
    def _valid(self, s: str, left: int, right: int) -> bool:
        while left < right:
            if (s[left] != s[right]):
                return False
            else:
                left += 1
                right -= 1
        return True

if __name__ == '__main__':
    s = "iffia"
    out = Solution().validPalindrome(s)
    print(out)