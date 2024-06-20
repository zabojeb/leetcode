class Solution:
    def calculate(self, position, m, mid):
        count = 1
        prev = position[0]
        for i in range(1, len(position)):
            if position[i] - prev >= mid:
                count += 1
                prev = position[i]
        return count >= m

    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        l = 1
        r = position[-1] - position[0]

        while r - l > 1:
            mid = (l + r) // 2
            if self.calculate(position, m, mid):
                l = mid
            else:
                r = mid - 1
        if self.calculate(position, m, r):
            return r
        return l