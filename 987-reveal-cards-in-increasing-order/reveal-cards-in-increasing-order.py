from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()

        n = len(deck)
        ans = [0] * n

        queue = deque(range(n))
        
        for card in deck:
            ans[queue.popleft()] = card
            if queue:
                queue.append(queue.popleft())
        
        return ans
