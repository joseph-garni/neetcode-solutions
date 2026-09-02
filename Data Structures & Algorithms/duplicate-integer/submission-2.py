class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for item in nums:
            if nums.count(item) > 1:
                return True
        return False
    