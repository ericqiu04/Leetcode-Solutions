import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        pattern = r'[^A-Za-z0-9]+'

        string = re.sub(pattern, '', s)
        string = string.lower()
        s1 = [a for a in string]
        s2 = [a for a in string]

        s1.reverse()

        print(s1)
        print(s2)
        if (s1 == s2):
            return True

        return False
