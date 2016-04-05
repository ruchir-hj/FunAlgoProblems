class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        product_of_all_ints_excpet_at_index = [None] * len(nums)
        
        product_so_far = 1
        i = 0
        while (i < len(nums)):
            product_of_all_ints_excpet_at_index[i] = product_so_far
            product_so_far *= nums[i]
            i += 1
        
        product_so_far = 1
        i = len(nums) - 1
        while(i >= 0):
            product_of_all_ints_excpet_at_index[i] *= product_so_far
            product_so_far *= nums[i]
            i -= 1
        
        return product_of_all_ints_excpet_at_index
