'''
@author:noc
@time:2020年4月3日
@url:https://leetcode-cn.com/problems/string-to-integer-atoi/
'''
class Solution:
    _int_min = -2**31
    _int_max = 2**31 - 1
    def myAtoi(self, str: str) -> int:
        import re
        ret = re.match(r'^[+-]?\d+', str.lstrip())
        if not ret: return 0
        intret = int(ret.group())
        if intret > self._int_max or intret < self._int_min:
            return self._int_max if intret > 0 else self._int_min
        return intret

if __name__ == '__main__':
    input = ' +2'
    output = Solution().myAtoi(input)
    print(output)