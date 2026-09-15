class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = set()
        left = 0
        max_length = 0

        # right drives the exploration
        for right in range(len(s)):
            # If the current character is already in our window,
            # shrink from the left until the duplicate is evicted
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            # Now the window [left...right] is guaranteed to be unique
            seen.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length
