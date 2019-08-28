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
