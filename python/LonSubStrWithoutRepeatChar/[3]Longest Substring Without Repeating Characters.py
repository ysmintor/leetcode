#Given a string, find the length of the longest substring without repeating characters. 
#
# 
# Example 1: 
#
# 
#Input: "abcabcbb"
#Output: 3 
#Explanation: The answer is "abc", with the length of 3. 
# 
#
# 
# Example 2: 
#
# 
#Input: "bbbbb"
#Output: 1
#Explanation: The answer is "b", with the length of 1.
# 
#
# 
# Example 3: 
#
# 
#Input: "pwwkew"
#Output: 3
#Explanation: The answer is "wke", with the length of 3. 
#             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
# 
# 
# 
# 
#

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dct = dict()
        max_so_far = curr_max = start = 0
        for index, i in enumerate(s):
            if i in dct and dct[i] >= start:
                max_so_far = max(max_so_far, curr_max)
                #curr_max = index - dct[i]
                curr_max = index - dct[i]
                start = dct[i] + 1 # select the nearest one that not repeat at start element
            else:
                curr_max += 1
            dct[i] = index # store the coordinated position for value i

        return max(max_so_far, curr_max)
