class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0 
        max_n = 0

        for i in s:
            if i == "(":
                count += 1
                max_n = max(max_n, count)
            elif i == ")":
                count -= 1
        
        return max_n