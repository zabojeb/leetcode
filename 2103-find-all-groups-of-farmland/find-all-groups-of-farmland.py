class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        FARMLAND, LAND = 1, 0
        rows, cols = len(land), len(land[0])
        res = []
        for r1 in range(len(land)):
            for c1 in range(len(land[0])):
                if (r1 == 0 or land[r1-1][c1] == LAND) and (c1 == 0 or land[r1][c1-1] == LAND) and land[r1][c1] == FARMLAND:
                    r2, c2 = r1, c1

                    while r2 < rows and land[r2][c1] == FARMLAND:
                            r2 += 1
                    while c2 < cols and land[r1][c2] == FARMLAND:
                            c2 += 1
                    res.append([r1, c1, r2-1, c2-1])
        return res
