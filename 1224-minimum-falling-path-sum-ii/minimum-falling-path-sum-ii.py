class Solution:
    def minFallingPathSum(self, g: List[List[int]]) -> int:
        m = [(0, -1)]

        for r in g:
            q = ((v + m[m[0][1] == j][0], j) for j, v in enumerate(r))
            m = nsmallest(2, q)

        return m[0][0]
