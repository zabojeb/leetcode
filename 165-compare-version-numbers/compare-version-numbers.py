class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")

        v1 = [*map(int, v1)] + [0] * (249 - len(v1))
        v2 = [*map(int, v2)] + [0] * (249 - len(v2))

        return (v1 > v2) - (v1 < v2)
