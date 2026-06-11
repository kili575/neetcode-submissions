class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = dict()

        for i, n in enumerate(nums):
            idx[n] = i
        
        for i, n in enumerate(nums):
            val = target - n
            if val in idx and i != idx[val]:
                return [i, idx[val]]


            