
class Solution:
    def findKthLargest(self, nums, k):
        max_num = max(nums)
        min_num = min(nums)
        barr = [0]*(max_num - min_num + 1)  #定义一个桶，桶的长度为最大值减去最小值并加1
        for num in nums:
            barr[num - min_num] += 1        #桶的索引为该元素与最小值的差，对应的元素为该元素出现的次数.
        print(barr)
        count = 0
        for i in range(len(barr)-1, -1, -1): 
            count += barr[i]                 #count此时为1, 2...大的元素差
            if count >= k:                   #当count大于或者等于K时，则代表满足第k大的条件
                return min_num+i             #返回最小值加差的值即为最大值
        return -1
nums = [3,3,1,5,6,4]
k = 2
print(Solution.findKthLargest(Solution(), nums, k))