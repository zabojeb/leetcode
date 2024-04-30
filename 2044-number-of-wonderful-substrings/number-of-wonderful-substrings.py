class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        ans = 0
        bits = 0
        cnt = {0: 1}
        for c in word:
            bits ^= 1 << (ord(c) - ord("a"))

            if cnt.get(bits) is None:
                cnt[bits] = 0
            
            ans += cnt[bits]
            cnt[bits] += 1
            
            for i in range(11):
                if cnt.get(bits ^ (1 << i)) is not None:
                    ans += cnt[bits ^ (1 << i)]
        return ans
