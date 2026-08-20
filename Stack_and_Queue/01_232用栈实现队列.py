class MyQueue:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int):
        self.stack_in.append(x)
        
    def pop(self):
        """
        移除队列最顶端的元素，并返回这个元素
        """
        if self.empty():
            return None
        if self.stack_out:
            return self.stack_out.pop()
        else:
            for _ in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()

    def peek(self):
        """
        获取队列最顶端的元素
        """
        ans = self.pop()
        self.stack_out.append(ans)
        return ans

    def empty(self):
        """
        只要in或者out有元素，说明队列不为空
        """
        return not(self.stack_in or self.stack_out)
    