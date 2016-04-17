class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # count the occurences of characters and contain odd occurrences in it
        unpaired_characters = set()
        for char in s:
            if char in unpaired_characters:
                unpaired_characters.remove(char)
            else:
                unpaired_characters.add(char)
        
        return len(unpaired_characters) <= 1
