class Solution:
    def deckRevealedIncreasing(self, deck):
        deck.sort(reverse=True)
        result = [deck[0]]

        for card in deck[1:]:
            result = [card] + [result[-1]] + result[:-1]

        return result
