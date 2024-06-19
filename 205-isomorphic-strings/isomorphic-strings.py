class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        for i in range(len(s)):
            if s[i] not in s_dict and t[i] not in t_dict:
                s_dict[s[i]] = t[i]
                t_dict[t[i]] = s[i]
            elif s[i] in s_dict and s_dict[s[i]] != t[i]:
                return False
            elif t[i] in t_dict and t_dict[t[i]] != s[i]:
                return False
        return True