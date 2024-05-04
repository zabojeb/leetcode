class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        buckets = [0] * (limit + 1)
        start = 0
        end = len(buckets) - 1
        boats = 0

        for weight in people:
            buckets[weight] += 1

        while start <= end:
            while start <= end and buckets[start] <= 0:
                start += 1

            while start <= end and buckets[end] <= 0:
                end -= 1

            if buckets[start] <= 0 and buckets[end] <= 0:
                break

            boats += 1

            if start + end <= limit:
                buckets[start] -= 1

            buckets[end] -= 1

        return boats
