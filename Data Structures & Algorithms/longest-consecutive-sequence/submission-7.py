class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        num_set = set(nums)

        max_consecutive = 0

        for num in num_set:
            # valid - can be a start of a consecutive sequence
            if num-1 not in num_set:
                curr_consecutive = 1

                while num+1 in num_set:
                    curr_consecutive += 1
                    num += 1
                    
                max_consecutive = max(curr_consecutive, max_consecutive)

        return max_consecutive
