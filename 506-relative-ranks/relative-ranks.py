class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score, reverse=True)
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]

        ranks = []
        for n in score:
            place = sorted_score.index(n)
            if place < 3:
                ranks.append(medals[place])
            else:
                ranks.append(str(place + 1))

        return ranks
