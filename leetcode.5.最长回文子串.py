'''
@author:noc
@time:2020年4月9日
@url:https://leetcode-cn.com/problems/longest-palindromic-substring/
'''
'''
动态规划解法：首先我们定义一个dp数组，dp【i】【j】保存的是，s[i, j]是否是一个回文串，对于回文串的判断，因为dp[i][j]始终是一个回文串，对于一个字符而言，所以所有的dp[i][j]保存的是 True，
然后我们在找到状态转移，对于dp[i][j]为True而言，有如下条件 s[i] == s[j], s[i + 1] == s[j - 1]。。。直到我们 j - i < 3时我们才能判断这是一个回文串。
时间复杂度：O（N*N）
空间复杂度：O（N*N）
中心扩散：在使用中心扩散时需要考虑到回文串为奇数偶数的情况，奇数从s[i]直接开始向两边扩散，偶数从s[i] s[i + 1]开始扩散，这个算法比较好理解。
时间复杂度：O（N*N）    
空间复杂度：O（1）
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        动态规划
        size = len(s)
        if size < 2:
            return s
        dp = [[False for _ in range(size)] for _ in range(size)]
        for i in range(size):
            dp[i][i] = True
        start = 0
        max_len = 1
        for j in range(size):
            for i in range(j):
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    dp[i][j] = (s[i] == s[j] and (j - i < 3 or dp[i + 1][j - 1]))   # 状态转移方程
                if dp[i][j] and j - i + 1 > max_len:    # 更新最长回文串的长度
                    start, max_len = i, j - i + 1
        return s[start:start + max_len]
        '''
        size = len(s)   
        if size < 2:
            return s
        start, end = 0, 0
        L = 1
        for i in range(size):
            len1 = self.dispersal_center(s, i, i, size) # 为奇数的情况
            len2 = self.dispersal_center(s, i, i + 1, size) # 为偶数的情况
            L = max(len1, len2) # 找出最长的
            if L > end - start:
                start = i - (L - 1) // 2
                end = i + L // 2

        return s[start:end + 1]

    def dispersal_center(self, s, left, right, size):
        while left >= 0 and right < size and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1 # right - left + 1 - 2


if __name__ == '__main__':
    s = 'ababa'
    out = Solution().longestPalindrome(s)
    print(s)