class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        people = list(range(1, n + 1))

        start = 0
        for i in range(n - 1):
            start = (start + k - 1) % len(people)
            people.pop(start)

        return people[0]
