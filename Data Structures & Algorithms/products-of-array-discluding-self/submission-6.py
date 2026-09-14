from collections import Counter

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # length of our array
        n = len(nums)

        prefix = [0] * n
        suffix = [0] * n
        result = [0] * n

        # first item each each end of the suffix will be 1 idk why
        # we already start each index (first element of each i.e. index 0- for prefixc and index n-1 at suffix to 1 for mathematical identity, so we can then set the ranges as seen below n-2 for suffix and 1 to n-1 for prefix)
        prefix[0] = suffix[n-1] = 1

        for i in range(1, n):
            prefix[i] = nums[i-1] * prefix[i-1]

        for i in range(n-2, -1, -1):
            suffix[i] = nums[i+1] * suffix[i+1]

        for i in range(n):
            result[i] = prefix[i] * suffix[i]

        return result

        # equal length prefix and suffix arrays to store each complementary value for when we want to make the sum



