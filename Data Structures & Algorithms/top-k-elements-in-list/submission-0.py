class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()
        output = []
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1
        sorted_count = dict(sorted(count.items(), key=lambda item: item[1]))
        count_list = list(sorted_count.keys())

        for i in range(k):
            output.append(count_list[-1-i])
        return output