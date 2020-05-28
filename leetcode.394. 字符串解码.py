"""
author: noc
time: 2020年5月28日
url: https://leetcode-cn.com/problems/decode-string/
"""

"""
算法流程：
构建辅助栈 stack， 遍历字符串 s 中每个字符 c；
当 c 为数字时，将数字字符转化为数字 multi，用于后续倍数计算, multi对应的就是后面 [] 里出现几次；
当 c 为字母时，在 res 尾部添加 c；
当 c 为 [ 时，将当前 multi 和 res 入栈，并分别置空置 00：
    记录此 [ 前的临时结果 res 至栈，用于发现对应 ] 后的拼接操作；
    记录此 [ 前的倍数 multi 至栈，用于发现对应 ] 后，获取 multi × [...] 字符串。
    进入到新 [ 后，res 和 multi 重新记录。
当 c 为 ] 时，stack 出栈，拼接字符串 res = last_res + cur_multi * res，其中:
    last_res是上个 [ 到当前 [ 的字符串，例如 "3[a2[c]]" 中的 a；
    cur_multi是当前 [ 到 ] 内字符串的重复倍数，例如 "3[a2[c]]" 中的 2。
    而我们此时res保存的就是字符‘c’
返回字符串 res。
"""

class Solution:
    def decodeString(self, s: str) -> str:
        st, multi, res = [], 0, ''  ## st里存的是元组（multi，last_res）multi = 后面 [] 里出现几次的次数, last_res = 上一个[ 到 multi所在位置内的字符
        for c in s:
            if c == '[':    ## 遇到 [ 入栈
                st.append((multi, res))
                multi, res = 0, ''
            elif c == ']': ## 出栈
                curr_multi, last_res = st.pop()
                res = last_res + curr_multi * res
            elif '0' <= c <= '9':   ## 更新multi
                multi = 10 * multi + int(c)
            else:
                res += c
        return res

if __name__ == '__main__':
    s = "3[a]2[bc]"
    out = Solution().decodeString(s)
    print(out)