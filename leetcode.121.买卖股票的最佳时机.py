'''
@author: noc
@time: 2020年3月9日
@url: https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/
'''
class Solution:
    def maxProfit(self, prices):
        profit = 0  # 利润
        sale = 0    # 卖出
        for i in range(len(prices) - 1, -1, -1):
            sale = max(sale, prices[i])     # 记录最大的卖出价格
            profit = max(profit, sale - prices[i])  # 更新利润的最大值
        return profit

if __name__ == "__main__":
    out = Solution().maxProfit([2,1,2,0,1]) # [2,1,2,0,1]
    print(out)

