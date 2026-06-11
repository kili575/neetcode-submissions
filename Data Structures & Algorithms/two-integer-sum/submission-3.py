class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tempDict = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in tempDict:
                return [tempDict[diff], i]
            tempDict[n] = i