class Solution:

    def tribonacci(self, n):

        def tri(n):
            if n >=0:
                if n <=1:
                    return n
                else:
                    return tri(n-1) + tri(n-2) + tri(n-3)
            return 0

        return tri(n)

      