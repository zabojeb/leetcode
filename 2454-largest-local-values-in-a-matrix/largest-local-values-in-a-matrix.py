class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        maxLocalMatrix = []

        for i in range(n - 2):
            maxLocalRow = []
            for j in range(n - 2):
                maxLocalRow.append(max(
                    grid[i][j], grid[i][j+1], grid[i][j+2],
                    grid[i+1][j], grid[i+1][j+1], grid[i+1][j+2],
                    grid[i+2][j], grid[i+2][j+1], grid[i+2][j+2]
                ))
            maxLocalMatrix.append(maxLocalRow)

        return maxLocalMatrix