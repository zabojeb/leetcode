class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse=True)
        result = [deck[0]]

        for card in deck[1:]:
            result.insert(0, result.pop())
            result.insert(0, card)

        return result
