class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0

        for num in nums:
            ans = ans | num

        return ans << (len(nums) - 1)
