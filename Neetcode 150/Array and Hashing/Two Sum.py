class Solution:

	def twoSum(self, nums: List[int], target: int) -> List[int]:

		for i in range(len(nums)):

			for n in range(1,len(nums)):

				if(i == n):
					pass

				if (nums[i] + nums[n]) == target:

					return [i,n]