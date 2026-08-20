class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for item in s:
            if item == '(':
                stack.append(')')
            elif item == '[':
                stack.append(']')
            elif item == '{':
                stack.append('}')
            elif not stack or stack[-1] != item:  # 当前遇到的是一个右括号，但是栈为空，或者栈顶期待的右括号和当前右括号不一致，那么字符串一定不合法。
                return False
            else:
                stack.pop()

        return True if not stack else False