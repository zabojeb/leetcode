class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        left, right = 0, 0
        while left < len(s) and right < len(t):
            if s[left] == t[right]:
                right += 1
            left += 1
        return len(t) - right
