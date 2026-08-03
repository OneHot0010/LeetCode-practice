from typing import List


class Solution:
    def towSum(self, nums: List[int], target: int) -> List[int]:

        records = dict()

        for index, value in enumerate(nums):
            if target - value in records:
                return [records[target - value], index]
            records[value] = index
        return []



if __name__ == "__main__":

    nums = [2,7,1,8]
    target = 9
