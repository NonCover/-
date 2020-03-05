# @author: noc
# @time: 2020年3月5日11点09分
# @url: https://leetcode-cn.com/problems/distribute-candies-to-people/

class Solution(object):
    def distributeCandies(self, candies, num_people):
        '''
        # 1. 暴力法
        people = [ 0 for _ in range(num_people) ]
        j = 1
        while candies != 0:
            for i in range(num_people):
                if candies - j <= 0:
                    people[i] += candies
                    return people
                if candies - j > 0:
                    people[i] += j
                    candies -= j
                    j += 1                   
        return people
        '''
        # 2. 等差数列求和法
        # 第n项发的糖果为 an = a1 + (n - 1)d
        n = num_people  # 公差
        p = int((2 * candies - 0.25)**0.5 - 0.5)    # p 为要发多少次的次数
        remaining = candies - p * (p + 1) // 2   # 最后一个人分不够所得
        # rows 代表完整发完num_people 次数， 由于会有发不完的时候，所以cols代表最后一个轮发几个人 
        rows, cols = p // n, p % n 
        d = [0] * n
        for i in range(n):
            d[i] = rows * (i + 1) + n * rows * (rows - 1) // 2
            if i < cols:
                d[i] += i + 1 + rows * n
        d[cols] += remaining
        return d

if __name__ == "__main__":
    out = Solution().distributeCandies(76, 5)
    print(out)