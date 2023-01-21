class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nSet = set(nums)
        longest = 0

        for i in nums:
            if (i - 1) not in nSet:
                length = 1
                while (i + length) in nSet:
                    length += 1

                longest = max(length, longest)

        return longest
