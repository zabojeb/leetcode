class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maximum = -math.inf
        
        window = sum(nums[:k])
        for i in range(len(nums) - k + 1):
            avg = window / k

            if avg > maximum:
                maximum = avg

            window -= nums[i]
            try:
                window += nums[i + k]
            except:
                break

        return maximum
