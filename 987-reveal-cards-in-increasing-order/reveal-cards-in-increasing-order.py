# Omg, its way too elegant

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        q = collections.deque()

        for card in sorted(deck, reverse=True):
            q.rotate()
            q.appendleft(card)

        return list(q)