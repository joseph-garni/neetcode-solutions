from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums) # O(n) time complexity

        # initalise min-heap
        heap = []

        for key, freq in count.items():
            heapq.heappush(heap, (freq, key))

            if len(heap) > k:
                heapq.heappop(heap)

        
        return [key for freq, key in heap]

        







        

