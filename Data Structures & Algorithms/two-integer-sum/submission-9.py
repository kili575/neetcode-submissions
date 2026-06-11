class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_nums = {}

        for i in range(len(nums)):
            dict_nums[nums[i]] = i
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in dict_nums.keys() and i != dict_nums[diff]:
                return [i, dict_nums[diff]]