class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]

        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1

        for c, v in count.items():
            freq[v].append(c) 
            
        result = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result
