# @author: noc
# @time: 2020年3月8日10点24分
# @url: https://leetcode-cn.com/problems/coin-change/

class Solution(object):
    def coinChange(self, coins, amount):
        if amount == 0: return 0
        self.ret = float("inf")  # 答案
        coins.sort()
        coins = coins[::-1] # 由大到小排序  
        #利用 bfs 遍里每一种情况, 不符合情况的剪枝
        def dfs(i, count, money):
            if money == 0:
                self.ret = min(self.ret, count)
                return
            for j in range(i, len(coins)):
                # 上一种情况需要的硬币数，减去现在所选的硬币数，则为你还能选的硬币数，当前最大币值 * 还能选的数如果还小于
                # mone的话，说明，即使后面得到结果，所需的硬币数也只能大于 ret 了
                if (self.ret - count) * coins[j] < money: 
                    break
                if coins[j] > money:    # 钱找不开
                    continue
                dfs(j, count+1, money - coins[j])

        for i in range(len(coins)):
            dfs(i, 0, amount)
        
        if self.ret == float("inf"):
            return -1
        return self.ret

if __name__ == "__main__":
    out = Solution().coinChange([1, 7, 10], 14)
    print(out)