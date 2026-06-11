class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = dict()

        for i, n in enumerate(nums):
            val = target - n
            if val in idx:
                return [idx[val], i]
            idx[n] = i


            