class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        new_list = list(set(nums))
        print(new_list)
        answer = []
        long_value = 0
        while len(answer) < k:
            longest = 0
            for i in new_list:
                if nums.count(i) > longest:
                    longest = nums.count(i)
                    long_value = i

            if long_value != "":
                new_list.remove(long_value)
            answer.append(long_value)

        return answer

#Time Limit Exceeded