class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        def largestRectangleArea(heights):
            stack = []
            max_area = 0
            heights.append(0)
            for i, h in enumerate(heights):
                while stack and h < heights[stack[-1]]:
                    height = heights[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, height * width)
                stack.append(i)
            return max_area

        max_area = 0
        n = len(matrix)
        m = len(matrix[0])
        heights = [0] * m

        for i in range(n):
            for j in range(m):
                heights[j] = heights[j] + 1 if matrix[i][j] == "1" else 0
            max_area = max(max_area, largestRectangleArea(heights))

        return max_area
