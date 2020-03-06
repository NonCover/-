# @author: noc
# @time: 2020年3月6日14点06分
# @url: https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/

class Solution(object):
    def findContinuousSequence(self, target):
        ret = []
        # # 双指针 滑窗思想
        # i = 1   # 左指针
        # j = 2   # 右指针
        # Sum = i + j
        # while i <= target // 2:
        #     # （target // 2）+ 1 + （target // 2） + 2 不可能 大于 target
        #     if Sum < target:
        #         j += 1  # 因为 sum（i -> j） 小于 target，需要移动 右指针增大和
        #         Sum += j
        #     elif Sum > target:
        #         i += 1
        #         Sum -= i - 1    # 总和大于 target， 移动左指针，让总和变小
        #     else:
        #         a = list(range(i, j+1))
        #         ret.append(a)
        #         Sum -= i
        #         i += 1
        # return ret

        # 求根法，利用等差数列
        # mid = target // 2 + 1
        # for y in range(2, mid + 1):
        #     x = (0.25 + y**2 + y - 2 * target)**0.5 + 0.5
        #     # if type(x) != complex   
        #     if type(x) != complex and x - int(x) == 0:
        #         a = list(range(int(x), y+1))
        #         ret.append(a)

        # 间隔法：通过等查数列一系列公式推断出来
        i = 1
        while i * (i + 1) / 2 < target:     
            if (target - (i * (i + 1) / 2)) % (i + 1) == 0:  # 整数
                x = int((target - (i * (i + 1) / 2)) // (i + 1))
                ret.append(list(range(x, x + i + 1)))
            i += 1
        return ret

if __name__ == "__main__":
    out = Solution().findContinuousSequence(3)
    print(out)
