class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        finalArray = []
        sArray = strs

        while len(sArray) > 0:
            sortArray = []
            indexString = [a for a in sArray[0]]
            indexString.sort()

            for s in sArray[1:]:
                string2 = [l for l in s]
                string2.sort()
                if (string2 == indexString):
                    sortArray.append(s)
                    sArray.remove(s)

            sortArray.append(sArray[0])
            finalArray.append(sortArray)
            sArray.remove(sArray[0])

        return finalArray