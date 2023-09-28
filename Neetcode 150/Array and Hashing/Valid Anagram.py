

class Solution(object):

    def mySolution(self, s, t):
        s1 = list(s)
        s2 = list(t)

        for i in s2:
            if i in s1:
                s1.remove(i)
            else:
                return False

        if s1:
            return False

        return True

    def optimalSolution(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT