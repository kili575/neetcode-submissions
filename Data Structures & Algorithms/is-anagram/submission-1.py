class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sort_t = sorted(t)
        sort_s = sorted(s)
        if len(sort_t) != len(sort_s):
            return False
        for l in range(len(sort_t)):
            if sort_t[l] != sort_s[l]:
                return False
        return True
        