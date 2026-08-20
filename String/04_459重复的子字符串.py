

# 移动匹配法
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) <= 1:
            return False

        new_s = s + s

        return s in new_s[1:-1]