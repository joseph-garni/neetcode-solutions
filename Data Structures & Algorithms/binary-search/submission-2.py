class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:
            cut = left + ( (right - left) // 2 )

            if nums[cut] == target:
                return cut

            if nums[cut] < target:
                left = cut + 1

            if nums[cut] > target:
                right = cut - 1
                
        return - 1

               
        