class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1:
            return 0

        def get_safeness_grid(n, grid):
            safeness_grid = [[0] * n for _ in range(n)]

            q = deque()
            visited = set()
            for i in range(n):
                for j in range(n):
                    if grid[i][j] == 1:
                        q.appendleft((0, i, j))
                        visited.add((i, j))

            while q:
                dist, i, j = q.pop()
                for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    x = i + dx
                    y = j + dy
                    if 0 <= x < n and 0 <= y < n and (x, y) not in visited:
                        visited.add((x, y))
                        safeness_grid[x][y] = dist + 1
                        q.appendleft((dist + 1, x, y))

            return safeness_grid

        def find_safeness(n, safeness_grid):
            safeness = min(safeness_grid[0][0], safeness_grid[-1][-1])
            h = [(-safeness, 0, 0)]
            visited = {(0, 0)}

            while h:
                current_safeness, i, j = heapq.heappop(h)
                current_safeness *= -1
                if current_safeness < safeness:
                    safeness = current_safeness

                for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    x = i + dx
                    y = j + dy
                    if 0 <= x < n and 0 <= y < n and (x, y) not in visited:
                        if x == y == n - 1:
                            return safeness
                        visited.add((x, y))
                        new_safeness = safeness_grid[x][y]
                        heapq.heappush(h, (-new_safeness, x, y))

        safeness_grid = get_safeness_grid(n, grid)
        return find_safeness(n, safeness_grid)
