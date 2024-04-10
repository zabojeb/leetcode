class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse=True)
        result = deque()

        for card in deck:
            if result:
                result.appendleft(result.pop())
                
            result.appendleft(card)

        return list(result)