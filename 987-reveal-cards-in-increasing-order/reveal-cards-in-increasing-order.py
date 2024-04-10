class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        n = len(deck)
        ans = [0] * n
        indices = list(range(n))
        
        i = 0
        while indices:
            ans[indices.pop(0)] = deck[i]
            if indices:
                indices.append(indices.pop(0))
            i += 1
        
        return ans
