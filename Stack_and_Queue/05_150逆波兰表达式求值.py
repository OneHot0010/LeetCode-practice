from operator import add, sub, mul
from typing import List

def div(x, y):
    return int(x / y) if x * y > 0 else -(abs(x) // abs(y))


class Solution(object):
    op_map = {"+": add, "-": sub, "*": mul, "/": div}

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in {'+', '-', '*', '/'}:
                stack.append(int(token))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(self.op_map[token](op1, op2))
        return stack.pop()
