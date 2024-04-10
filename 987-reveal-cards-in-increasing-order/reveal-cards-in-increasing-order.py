class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        ans = deque([deck.pop()])
        
        deck.reverse()
        for card in deck:
            ans.appendleft(ans.pop())
            ans.appendleft(card)

        return list(ans)