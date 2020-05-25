"""
author: noc
time: 2020年5月25日
url: https://leetcode-cn.com/problems/lru-cache/
"""
"""
所谓LRU缓存机制，通俗地讲就是，我们每次淘汰掉最久没有使用得数据，保存最新使用的数据。
在这里我们不用Python的库，自己造轮子来解这道题。我们首先需要一个双向链表来保存cache，然后用一个哈希表来获取数据，这样才能保证O（N）的存取时间复杂度。
具体看代码实现，比较简单，就是设计数据结构较复杂
"""

class Node:
    def __init__(self, k: int, v: int, prev = None, next = None) -> None:
        self.k = k
        self.v = v
        self.prev = prev
        self.next = next

class DoubleLinked(object):
    def __init__(self):
        """
        初始化首尾节点
        """
        self.head, self.tail = Node(0, 0), Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def addFrist(self, x: Node) -> None:
        """把新节点加入到头部"""
        x.next = self.head.next
        x.prev = self.head
        self.head.next.prev = x
        self.head.next = x
        self.size += 1

    def remove(self, x: Node) -> None:
        """删除该节点"""
        x.prev.next = x.next
        x.next.prev = x.prev
        self.size -= 1

    def removeLast(self) -> Node:
        """删除尾节点，并返回这个节点"""
        last = self.tail.prev
        if last == self.tail: return
        self.remove(last)
        return last

import collections
class LRUCache:
    def __init__(self, capacity: int):
        ## 相当于Java中的 new HashMap<Integer, Node>();
        self.map = collections.defaultdict(Node)
        self.cache = DoubleLinked()
        self.maxSize = capacity

    def get(self, key: int) -> int:
        """
        我们得到key的值，如果不存在这个key，就返回-1，如果存在，就返回对应的值，
        并且，我们还要把这个key放在cache的首位
        """
        if key not in self.map.keys():
            return -1
        val = self.map[key].v
        ## 利用put方法，将这个key的节点放在cache首位
        self.put(key, val)
        return val

    def put(self, key: int, value: int) -> None:
        x = Node(key, value)
        if key in self.map.keys():
            self.cache.remove(self.map[key])    ## 删除key对应的节点
        else:
            ## 达到缓存最大空间，需要删除一个最久为访问的节点，相当于删除cache最后一个节点
            if self.cache.size == self.maxSize:
                last = self.cache.removeLast()
                self.map.pop(last.k)

        self.map[key] = x
        self.cache.addFrist(x)

if __name__ == '__main__':
    cache = None
    method = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    data = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    ans = []
    for i in range(len(method)):
        met = method[i]
        if met == "LRUCache":
            cache = LRUCache(data[i][0])
            ans.append(None)
        elif met == "put":
            cache.put(data[i][0], data[i][1])
            ans.append(None)
        elif met == "get":
            out = cache.get(data[i][0])
            ans.append(out)
    print(ans)
