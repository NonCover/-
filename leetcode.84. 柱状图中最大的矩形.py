"""
author: noc
time: 2020年5月30日
url: https://leetcode-cn.com/problems/largest-rectangle-in-histogram/
"""

"""
单调栈：
为了得到最大矩形的面积，我们的栈一定的是递增的，我们循环数组，当前数组的高度小于栈顶元素对应的高度，我们就出栈。
需要注意的是，我们的栈底元素始终为 0 ，并且对应的高度也只能是 0 ，这样做的目的是，保证我们得到的答案为最大值。
例如[2, 1, 2], 我们如果栈底元素不设置为0的话，就会出错，此时答案应该为 3 ，可结果为 2 。
"""

class Solution:
    def largestRectangleArea(self, heights):
        st = [-1]     ## 单调栈
        heights = heights + [0]   ## 此步是为了防止循环完成后，栈内还有元素，可能造成答案出错
        ans = 0
        for i in range(len(heights)):
            ## 维护一个单调栈
            while st[-1] != -1 and heights[st[-1]] > heights[i]:
                idx = st.pop()
                ans = max(ans, (i - st[-1] - 1) * heights[idx]) ## 更新答案
            st.append(i)
        return ans

if __name__ == '__main__':
    heights = [2,1,2]
    out = Solution().largestRectangleArea(heights)
    print(out)
