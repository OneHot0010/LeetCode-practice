
'''
使用双指针在原数组上原地覆盖，实现元素的“逻辑删除”
'''
from typing import List

class Solution:
    def removeElement(nums: List[int], target: int) -> int:
         fast, slow = 0, 0
         size = len(nums)

         while fast < size:
            if nums[fast] != target:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow