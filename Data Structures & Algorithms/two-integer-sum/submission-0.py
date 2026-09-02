class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # val : index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return
        



        '''
        for i in range (0, len(nums)):
            if nums[i] + nums[i+1] == target:
                return [i, i+1]

        '''