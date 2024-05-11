class Solution:
    def mincostToHireWorkers(
        self, quality: List[int], wage: List[int], k: int
    ) -> float:
        ratios = []
        for i, j in zip(quality, wage):
            ratios.append((float(j) / i, i))

        ratios.sort()

        totQ = 0
        Qselected = []
        res = float("inf")
        
        for r, q in ratios:
            totQ += q
            Qselected.append(q)

            if len(Qselected) > k:
                Qselected = sorted(Qselected)
                if Qselected[-1] == q:
                    totQ -= Qselected[-2]
                    del Qselected[-2]
                else:
                    totQ -= Qselected[-1]
                    del Qselected[-1]

            if len(Qselected) == k:
                res = min(res, totQ * r)

        return res
