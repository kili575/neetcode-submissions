from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ls = defaultdict(int)
        lt = defaultdict(int)

        for i in s:
            ls[i] += 1
        for j in t:
            lt[j] += 1
        
        return ls == lt
            