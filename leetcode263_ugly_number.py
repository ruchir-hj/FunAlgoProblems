class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        
        if num == 1:
            return True
            
        for prime in [2,3,5]:
            while num % prime == 0:
                num = num /prime
        return num == 1
