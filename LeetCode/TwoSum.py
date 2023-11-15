# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         for i in range(len(nums)):
#             print(i)
#             for j in range(i+1, len(nums)):
#                 print(f"j {j}")
#                 if((nums[i]+nums[j])== target):
#                     return [i,j]
                
class Solution(object):
    def twoSum(self, nums, target):
        num_dict = {}
        for key, value in enumerate(nums):
            complement = target - value
            if complement in num_dict:
                return [num_dict[complement], key]
            # I get this wrong here because instead of num_dict[value], I use the complement
            # num_dict[value] is to saved the position of the value and index position to the num_dict
            num_dict[value] = key
        return None


    
test_result = Solution()

print(test_result.twoSum(nums=[7,3,9,9,2,3], target=6 ))