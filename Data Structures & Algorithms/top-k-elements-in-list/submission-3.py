class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)
        for n in nums:
            res[n] += 1
        res = dict(sorted(res.items(), key=lambda x: x[1], reverse=True))
        out = []
        for i, j in enumerate(res.keys()):
            if i >= k:
                break
            out.append(j)
        return out