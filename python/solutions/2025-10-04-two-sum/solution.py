from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for i, x in enumerate(nums):
            need = target - x
            if need in lookup:
                return [lookup[need], i]
            lookup[x] = i
        return []
