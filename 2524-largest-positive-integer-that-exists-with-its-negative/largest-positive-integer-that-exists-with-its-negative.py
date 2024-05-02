class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        pit = set(nums)
        ans = -1
        for i in pit:
            if -i in pit and i > ans:
                ans = i
        return ans
