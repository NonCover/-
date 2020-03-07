# @author: noc
# @time: 2020年3月7日17点15分
# @url: https://leetcode-cn.com/problems/dui-lie-de-zui-da-zhi-lcof/

import queue
# 双端队列 ＋ 辅助队列
class MaxQueue(object):
    def __init__(self):
        self.deque = queue.deque()  # 辅助队列
        self.queue = queue.Queue()  # 双端队列

    def max_value(self):
        # 因为双端数列以及是一个递减数列，所以直接取第一个即可
        return self.deque[0] if self.deque else -1

    def push_back(self, value):
        # 入队列，双端队列成一个递减队列
        # 辅助队列用来保存真正的队列
        self.queue.put(value)
        while self.deque and self.deque[-1] < value:
            self.deque.pop()    # 弹出比 value 小的值
        self.deque.append(value)    

    def pop_front(self):
        if not self.queue:
            return -1
        ret = self.queue.get()
        if ret == self.deque[0]:
            self.deque.popleft()
        return ret


if __name__ == "__main__":
    pass