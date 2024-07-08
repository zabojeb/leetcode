class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        curr = 0
        for i in range(2, n + 1):
            curr = (curr + k) % i
        
        return curr + 1