# solution 1
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if (len(s) != len(t)):
            return False
        s_dict = {}
        t_dict = {}
        for word in s:
            if (word not in s_dict.keys()):
                s_dict[word] = 1
            else:
                s_dict[word] = s_dict[word] + 1

        for word in t:
            if (word not in t_dict.keys()):
                t_dict[word] = 1
            else:
                t_dict[word] = t_dict[word] + 1

        for chkChar in s_dict.keys():
            if (chkChar not in t_dict or s_dict[chkChar] != t_dict[chkChar]):
                return False
        return True

# Solution 2
class Solution(object):
    def isAnagram(self, s, t):
        return (sorted(s) == sorted(t))

