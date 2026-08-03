from typing import List

# 左闭右开
class Solution:
    def binarySearch(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        middle = left + (right - left) // 2

        while left < right:
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                return middle
        
        return -1


# 左闭右闭
class Solution:
    def binarySearch(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        middle = left + (right - left) // 2

        while left <= right:
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                return middle
        return -1