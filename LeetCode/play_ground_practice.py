# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

class Solution(object):
    def twoSum(self, nums, target):
        # num_dict is to store key as the complement value and value is as the position
        num_dict = {}
        for key, value in enumerate(nums):
            complement = target - value
            # we find the complement
            # we return the current key and the complement position which is value of the num_dict
            if complement in num_dict:
                return [num_dict[complement], key]
            num_dict[value] = key

    
test_result = Solution()

print(test_result.twoSum(nums=[7,3,9,9,2,3], target=6 ))

