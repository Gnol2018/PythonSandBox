from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)
nums = [3, 2, 3, 3]
val = 3
result = Solution()
print(result.removeElement(nums, val))
