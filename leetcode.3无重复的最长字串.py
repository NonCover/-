#!/usr/bin/python
#-*- coding:utf-8 -*-
#__author__ = noc
#3.   
'''
   给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
示例 1:
输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
''' 
import time

def Timer(func):
    def wraper(s):
        start  = time.time()
        s = func(s)
        s.lengthOfLongestSubstring()
        end = time.time()
        return '执行时间:%s'%(end-start)
    return wraper

@Timer
class Solution:
    def __init__(self, s):
        super().__init__()
        self.s = s
    def lengthOfLongestSubstring(self):
        long_str = []
        long_num = []
        for i in self.s:
            if i in long_str:
                long_num.append(len(long_str))
                cur = long_str.index(i)
                long_str = long_str[cur+1:]
                long_str.append(i)

            if i not in long_str:
                long_str.append(i)
                long_num.append(len(long_str))
        print(max(long_num))

print(Solution('abcsdcmnbsdfsdgfaffasfvp'))