class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort array of numbers
        nums.sort()

        solutions = []

        n = len(nums)

        for i in range(n - 2):

            # if first item in nums (smallest) is greater than 0, terminate the loop
            if nums[i] > 0:
                break

            # skip duplicate values for the first element

            if i > 0 and nums[i] == nums[i-1]:
                continue # continue skips the rest of 
                # the code below in this iteration

            left = i + 1 # first item larger than our curr item in list
            right = n - 1 # end of list (largest value)

            # now we just reduce to 2Sum
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                # total smaller, need larger element, increment left
                if total < 0:
                    left += 1

                # total larger, need smaller element, decrease right by 1
                elif total > 0:
                    right -= 1

                # valid case
                else:
                    solutions.append([nums[i], nums[left], nums[right]])
                    # now appended, move each number in their respective direction
                    left += 1
                    right -= 1

                    # skip our duplicate values of left and right so we get unique arrays               
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # if new item ahead of left is equal, change the left value so we are checking a unique element (same for right below)

                    while left < right and nums[right] == nums[right+1]:
                        right -= 1

        return solutions

                

