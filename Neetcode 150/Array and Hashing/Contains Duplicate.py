class Solution(object):

    def mySolution(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = {}
        dup = 0
        for n in nums:
            if n not in count:
                count[index(n)] = n
            else:
                dup += 1

        if dup > 0:
            return True

        return False

    def optimalSolution(self, nums):
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
