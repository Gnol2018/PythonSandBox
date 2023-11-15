# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        # """
        insert_index = 0
        for i in range(len(nums)):
            if (nums[i] == target):
                insert_index = i
            else:
                insert_index = 0
        if insert_index == 0:
            nums.append(target)
            nums.sort()
            for i in range(len(nums)):
                if (nums[i] == target):
                    insert_index = i
                    break
                else:
                    insert_index = 0
        return insert_index
            

# nums = [1,5,3,5,9]
# target = 7
# test_solution = Solution()
# result = test_solution.searchInsert(nums=nums, target=target)

# print(result)

class SolutionBinarySearch(object):
    def searchInsert(self, nums, target):
        # left is 0
        # right is len(nums) - 1
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left

nums = [1,5,3,5,9]
target = 7
test_solution = SolutionBinarySearch()
result = test_solution.searchInsert(nums=nums, target=target)

print(result)