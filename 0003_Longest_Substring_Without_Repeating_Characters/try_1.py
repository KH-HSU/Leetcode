class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        maps = {}
        max_num = 0
        while i < len(s) and j < len(s):
            char = s[j:j+1] 
            if char in maps:
                max_num = max(max_num, j-i)
                i = i + 1
                j = i
                maps = {}
            else:
                j = j + 1
                maps[char] = 0
        max_num = max(max_num, j-i)
        return max_num