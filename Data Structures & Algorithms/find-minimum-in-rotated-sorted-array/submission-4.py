class Solution:
    def findMin(self, nums: List[int]) -> int:

        # cycle through all elements in the array

        # store the smallest current value

        left = 0
        right = len(nums) - 1

        while left < right:
            middle = left + (right-left) // 2

            if nums[middle] < nums[right]:
                right = middle

            else:
                left = middle + 1
        return nums[left]

        