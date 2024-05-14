class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        max_gold = 0

        def dfs(i, j, curr_gold):
            nonlocal max_gold
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return

            gold = grid[i][j]
            curr_gold += gold

            grid[i][j] = 0  # Mark as visited

            max_gold = max(max_gold, curr_gold)

            dfs(i + 1, j, curr_gold)
            dfs(i - 1, j, curr_gold)
            dfs(i, j + 1, curr_gold)
            dfs(i, j - 1, curr_gold)

            grid[i][j] = gold  # Backtrack

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    dfs(i, j, 0)

        return max_gold
