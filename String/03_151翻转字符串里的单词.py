class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()

        left, right = 0, len(words) - 1

        while left < right:
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1

        return " ".join(words)


'''
如果要求空间复杂度为 O(1)，则不能使用额外空间
Python 因为 str 不可变，必须转换成 list，因此无法做到严格 O(1)。
'''

class Solution1:
    def areverseWords(self, s: str) -> str:

        s = list(s)
        n = len(s)

        slow = 0
        fast = 0

        while fast < n:
            # 去除多余的空格
            while fast < n and s[fast] == " ":
                fast += 1

            while fast < n and s[fast] != ' ':
                s[slow] = s[fast]
                slow += 1
                fast += 1

            if fast < n:
                s[slow] = ' '
                slow += 1

        # 删除末尾的空格
        s = s[:slow]

        def reverse(left, right):
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right += 1

        # 翻转整个字符串
        reverse(0, len(s)-1)

        start = 0

        for i in range(len(s) + 1):
            if i == len(s) or s[i] == ' ':
                reverse(start, i-1)

        return ''.join(s)
