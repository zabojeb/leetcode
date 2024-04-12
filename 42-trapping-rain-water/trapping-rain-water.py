class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        result = 0
        
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while left < right:
            if left_max < right_max:
                result += left_max - height[left]
                left += 1
                left_max = max(left_max, height[left])
            else:
                result += right_max - height[right]
                right -= 1
                right_max = max(right_max, height[right])

        return result
