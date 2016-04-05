class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        cur = 0
        res = 0
        d = {}
        for i, c in enumerate(s):
            if c not in d:
               cur += 1
            else:
               cur = min(i - d[c], cur + 1)
            d[c] = i
            res = max(cur, res)
        return res
                
