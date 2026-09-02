from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # we need to group any anagrams 

        # we can use a set to order each item

        # each anagram has the same set

        # we basically have a many to one relationship 
        # between strs and possibleSets

        ans = []

        # we want to look at each item in strs
        # determine if its set has been seen before
        # store its position in a set, and 
        # yeah we can just store a map (set(word), [list of keys])

        hashMap = defaultdict(list)

        for word in strs:
            setValue = str(sorted(word))
            hashMap[setValue].append(word)

        for key, value in hashMap.items():
            ans.append(value)

        return ans
            
