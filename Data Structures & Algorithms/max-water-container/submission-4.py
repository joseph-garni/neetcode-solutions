class Solution:
    def maxArea(self, heights: List[int]) -> int:
        

        # two pointers

        # define an algorithm where we can find the max height.

        max_val = 0

        left = 0
        right = len(heights) - 1

        while left < right:

            # this is how we define area of course
            area = min(heights[right], heights[left]) * (right - left)

            max_val = max(area, max_val)

            # test what happens by changing left or right

            # test moving pointer with smaller value

            if heights[left] < heights[right]:
                left += 1

            else:
                right -= 1

        return max_val
            