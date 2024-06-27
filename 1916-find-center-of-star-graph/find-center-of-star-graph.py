class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        arr = edges[0] + edges[1]

        for i in range(4):
            if arr[i] in arr[:i]:
                return arr[i]
        return -1