class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = {}

        for i, num in enumerate(nums):
            if target - num in pairs:
                return [i, pairs[target - num]]

            pairs[num] = i
        
        return []