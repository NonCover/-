'''
@author:noc
@time:2020年4月5日
@url:https://leetcode-cn.com/problems/lfu-cache/
'''
from collections import OrderedDict
from collections import defaultdict
'''
解法：用一个默认字典嵌套一个有序字典，默认字典存放访问次数的键，有序字典存放每一次 put 和 get 操作的键，有序字典是根据插入先得放在前面来排序得，因为我们插入后，超出默认长度时，我们需要
删除一个不经常访问的键，如果有两个键的访问次数相同，这个时候我们需要通过有序字典来删除相同访问次数下最先访问的键
'''

class LFUCache:
    """
    @param: capacity: An integer
    """

    def __init__(self, capacity):
        self.mincount = 0
        self.capacity = capacity
        self.cache = {}
        self.visited = {}
        # 默认字典嵌套一个有序字典，外层字典的键是访问次数，有序字典会根据放入元素的先后顺序进行排序
        self.key_list = defaultdict(OrderedDict)

    def put(self, key, value):
        # write your code here
        # 如果该key已经存在，修改value并且次数+1
        if self.capacity == 0: return None
        if key in self.cache:
            self.cache[key] = value
            self.get(key)
            return

        # 如果缓存满了，则删除最少访问次数
        if len(self.cache) == self.capacity:
            # 找到最小访问次数
            temp_key, tmep_val = next(iter(self.key_list[self.mincount].items()))
            del self.cache[temp_key]
            del self.visited[temp_key]
            del self.key_list[self.mincount][temp_key]

            self.cache[key] = value
            self.visited[key] = 0

        # 添加时默认都是1，所以都放在访问次数为1的层中
        self.mincount = 1
        self.cache[key] = value
        self.visited[key] = 1
        # 对记录字典进行赋值{1：{key:none, key1:none}}
        self.key_list[1][key] = None

    def get(self, key):
        # write your code here
        if key not in self.cache:
            return -1

        # 取出该key的访问次数
        count = self.visited[key]
        # 对访问次数进行+1
        self.visited[key] += 1
        # 对记录字典进行更新
        self.key_list[count].pop(key)
        self.key_list[count + 1][key] = None

        # 如果访问次数等于最小访问次数，并且该次数下已经没有值了，则最小访问次数+1，为下次加入做准备
        if count == self.mincount and len(self.key_list[count]) == 0:
            self.mincount += 1

        return self.cache[key]

if __name__ == '__main__':
    cache = LFUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.get(1)
    cache.put(3, 3)
    cache.get(2)
    cache.get(3)
    print(cache.key_list)

    cache.put(4, 4)
    cache.get(1)
    print(cache.cache)
    cache.get(3)
    cache.get(4)


