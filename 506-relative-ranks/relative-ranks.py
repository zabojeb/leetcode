class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        return [
            medals[i] if i < 3 else str(i + 1)
            for i in [sorted(score, reverse=True).index(n) for n in score]
        ]
