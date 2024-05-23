class Solution:
    def beautifulSubsets(self, a: List[int], k: int) -> int:
        def subset(a, b, i):
            if i < len(a):
                result = subset(a, b, i + 1)

                if a[i] - k not in b:
                    result += subset(a, b + [a[i]], i + 1)

                return result

            return len(b) > 0

        return subset(sorted(a), [], 0)
