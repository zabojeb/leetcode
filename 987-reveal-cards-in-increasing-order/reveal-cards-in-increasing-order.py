class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        result = collections.deque()

        for card in reversed(sorted(deck)):
            result.rotate()
            result.appendleft(card)

        return list(result)