class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = -1
        l = 0

        for i in xrange(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                k = i

        if k == -1:
            nums.reverse()
            return

        for i in xrange(k + 1, len(nums)):
            if nums[i] > nums[k]:
                l = i

        nums[k], nums[l] = nums[l], nums[k]
        nums[k+1:] = nums[k+1:][::-1]
