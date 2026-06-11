class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictNums = {}
        for n, i in enumerate(nums):
            dictNums[i] = n
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in dictNums and i != dictNums[diff]:
                return [i, dictNums[diff]]
        return False