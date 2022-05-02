class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums=[i**2 for i in nums]
        nums.sort()
        return nums
