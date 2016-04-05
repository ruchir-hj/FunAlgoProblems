class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n = len(nums1) + len(nums2)
        if (n % 2 == 1):
            return self.kth(nums1, nums2, n // 2)
        else:
            return (float(self.kth(nums1, nums2, n // 2  - 1)) + float(self.kth(nums1, nums2, n // 2)))/2.0
        
    def kth(self, a, b, k):
        if not a:
            return b[k]
        if not b:
            return a[k]
            
        midA, midB = len(a) // 2, len(b) // 2
            
        if midA + midB < k:
            if a[midA] > b[midB]:
                return self.kth(a, b[midB + 1:], k - midB - 1)
            else:
                return self.kth(a[midA + 1:], b, k - midA - 1)
        else:
            if a[midA] > b[midB]:
                return self.kth(a[:midA], b, k)
            else:
                return self.kth(a, b[:midB], k)
            
            
        
