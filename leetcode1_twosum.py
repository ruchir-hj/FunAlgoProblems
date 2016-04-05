# solution 1

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = dict()
        for i in range(len(nums)):
            key = target - nums[i]
            if key in d:
                return [d[key] + 1, i + 1]
            else:
                d[nums[i]] = i
        return []

# solution 2
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = dict()
        for i, num in enumerate(nums):
            key = target - num
            if key in d:
                return [d[key] + 1, i + 1]
            else:
                d[num] = i
        return []
        
