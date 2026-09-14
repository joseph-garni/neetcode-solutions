class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n # Handles k > n and k == n automatically

        def reverse(start: int, end: int):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        # 1. first reverse the whole array
        reverse(0, n-1)

        # 2. reverse first k elements
        reverse(0, k-1)

        # 3. reverse the k to n elements
        reverse(k, n-1)







