from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        ans = deque([deck.pop()])
        
        for card in reversed(deck):
            ans.appendleft(ans.pop())
            ans.appendleft(card)

        return list(ans)