from queue import Queue

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        q = Queue()

        for card in reversed(sorted(deck)):
            if not q.empty():
                q.put(q.get())
            q.put(card)

        return reversed(list(q.queue))

