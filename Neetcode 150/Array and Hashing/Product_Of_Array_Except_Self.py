class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        returnArray = []
        for i in range(len(nums)):
            leftSide = nums[:i]
            rightSide = nums[i + 1:]
            leftTot = 1
            rightTot = 1
            for l in leftSide:
                leftTot = leftTot * l

            for r in rightSide:
                rightTot = rightTot * r

            total = leftTot * rightTot
            returnArray.append(total)

        return returnArray