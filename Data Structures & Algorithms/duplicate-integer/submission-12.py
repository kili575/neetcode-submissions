class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_nums = set()
        for i in range(len(nums)):
            set_nums.add(nums[i])
            if len(set_nums) != i+1:
                return True
        return False