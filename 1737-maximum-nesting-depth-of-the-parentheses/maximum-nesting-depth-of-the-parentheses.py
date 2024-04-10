class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0 
        max_n = 0

        for i in s:
            if i == "(":
                count += 1
                if max_n < count:
                    max_n = count
            elif i == ")":
                count -= 1
        
        return max_n
        