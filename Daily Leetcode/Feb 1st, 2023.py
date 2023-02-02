class Solution(object):

    def gcdOfStrings(self, str1, str2):
        """
:type str1: str
:type str2: str
:rtype: str
"""
        len1, len2 = len(str1), len(str2)

        def isDivisors(i):

            if len1 % i or len2 % i:
                return False

            l1, l2, = len1 / i, len2 / i
            return (str1[:i] * l1 == str1 and str1[:i] * l2 == str2)

        for i in range(min(len1, len2), 0, -1):
            if isDivisors(i):
                return str1[:i]

        return ""
