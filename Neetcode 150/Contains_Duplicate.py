class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        for i in range(len(nums)):
            for j in range(len(nums))[i + 1:]:
                if(nums[j] == nums[i]):
                    return True


        return False