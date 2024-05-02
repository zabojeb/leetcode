class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()

        l = 0
        r = len(nums) - 1
        
        while l < r:
            diff = nums[l] + nums[r]
            if diff > 0:
                r -= 1
            elif diff < 0:
                l += 1
            else:
                return nums[r]
                
        return -1
