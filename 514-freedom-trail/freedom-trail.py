class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        map = defaultdict(list)

        for i,s in enumerate(ring):
            map[s].append(i)

        m = len(ring)

        pre_pos,pre_step = [0],[0]

        for k in key:
            next_pos = map[k]
            next_step = [inf] * len(next_pos)
            
            for j,n in enumerate(next_pos):
                for k,p in enumerate(pre_pos):
                    next_step[j] = min(next_step[j],1 + pre_step[k] + 
                                    (min(abs(n-p),abs(n-p-m)) if n > p else min(abs(p-n),abs(p-n-m))))
            pre_pos = next_pos
            pre_step = next_step

        return min(pre_step)