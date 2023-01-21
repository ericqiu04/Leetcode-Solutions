class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        string1 = [a for a in s]
        string2 = [b for b in t]

        string1.sort()
        string2.sort()

        if string1 == string2:
            return True

        else:
            return False

