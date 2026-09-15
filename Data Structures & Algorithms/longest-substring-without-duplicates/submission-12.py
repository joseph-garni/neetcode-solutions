class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # we can just store seen values in a hashset

        if len(s) == 0:
            return 0

        elif len(s) == len(set(s)):
            return len(s)

        else:

            seen = set()

            left, right, max_length = 0, 0, 0

        # first add the first element to the list

        # condition to keep sliding/checking all elements
            while right < len(s):
                if s[right] not in seen:
                    seen.add(s[right])
                    right += 1
                    max_length = max(max_length, len(seen))
                else:
                    seen.remove(s[left])
                    left += 1
            
            return max_length
