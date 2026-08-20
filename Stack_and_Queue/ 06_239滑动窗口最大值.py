from collections import deque
from typing import List

class MyQueue:
    def __init__(self):
        self.queue = deque()  # 这里需要使用 dequeue 实现单调队列，直接使用 list 会超时

    # 每次弹出的时候，比较当前要弹出的数值是否等于队列出口元素的数值，如果相等则弹出
    #   如果即将离开窗口的那个元素，恰好等于单调队列的队头，才把它删除。
    #   只有“离开窗口的元素”刚好是当前最大值候选时，才需要从单调队列中删除它。
    # 同时 pop 之前判断队列当前是否为空
    def pop(self, value):
        if self.queue and value == self.queue[0]:
            self.queue.popleft()  # list.pop() 时间复杂度为 O(n), 治理需要使用 collections.deque()

    # 如果 push 的数值大于队尾的数值，那么就将队列后端的数值弹出，直到 push 的数值小于等于队列入口元素的数值为止
    # 这样就保持了队列里的数值是单调从大到小的了
    def push(self, value):
        while self.queue and value > self.queue[-1]:
            self.queue.pop()
        self.queue.append(value)

    # 查询当前队列里的最大值 直接返回队列前端也就是 front 就可以了
    def front(self):
        return self.queue[0]


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que = MyQueue()
        result = []

        for i in range(k):  # 先将前 k 的元素放进队列
            que.push(nums[i])
            
        result.append(que.front())  # result 记录前 k 的元素的最大值

        for i in range(k, len(nums)):
            que.pop(nums[i - k])  # 滑动窗口移除最前面元素
            que.push(nums[i])  # 滑动窗口前加入最后面的元素
            result.append(que.front())  # 记录对应的最大值

        return result