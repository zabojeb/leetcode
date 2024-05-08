class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        max_heap = [(-s, i) for i, s in enumerate(score)]
        heapq.heapify(max_heap)

        ranks = [""] * len(score)

        for i in range(len(score)):
            s, index = heapq.heappop(max_heap)
            if i == 0:
                ranks[index] = "Gold Medal"
            elif i == 1:
                ranks[index] = "Silver Medal"
            elif i == 2:
                ranks[index] = "Bronze Medal"
            else:
                ranks[index] = str(i + 1)

        return ranks
