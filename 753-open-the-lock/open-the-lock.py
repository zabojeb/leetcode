class Solution:
    def getNeighbors(self, s):
        res = []
        for i, c in enumerate(s):
            n = int(c)
            res.append(s[ : i] + str((n - 1) % 10) + s[i + 1 :])
            res.append(s[ : i] + str((n + 1) % 10) + s[i + 1 :])
        return res
        
    def openLock(self, deadends: List[str], target: str) -> int:
        marker, depth = "x", 0
        visited, q = set(deadends), deque(["0000"])
        
        while q:
            sz = len(q)

            for _ in range(sz):
                cur = q.popleft()

                if cur == target:
                    return depth

                if cur not in visited:
                    q.extend(self.getNeighbors(cur))
                    visited.add(cur)

            depth += 1

        return -1
