from collections import Counter

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        unique = []

        # frequency map of each item then just check if they are > 1
        count = Counter(arr)
        

        for i in range(len(arr)):
            if count[arr[i]] > 1:
                continue
            else:
                unique.append(arr[i])

        if len(unique) < k:
            return ""

        else:
            return unique[k-1]

        



            
        