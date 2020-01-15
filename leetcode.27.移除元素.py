# @author：noc
# @time：2020年1月15日
# @url：https://leetcode-cn.com/problems/remove-element/

def solution(nums, val):
    # 双指针
    i = 0 
    for j in range(0, len(nums)):
        if nums[j] != val:  # 当第 nums[j] 个等于val时，把nums[j] 赋值给 nums[i]，i加一
            nums[i] = nums[j]
            i += 1
    return nums[:i] # 返回去掉val的数组

if __name__ == "__main__":
    nums = [2, 3, 2, 1]
    val = 2
    print(solution(nums, val))