# /**
#  * @param {string[]} strs
#  * @return {string}
#  */

# // Input: strs = ["flower","flow","flight"]
# // Output: "fl"
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # Initialize the prefix
        prefix = ""

        # Check if the list is empty
        if not strs:
            return None

        # Iterate through characters of the first string in the list
        for i in range(len(strs[0])):
            # loop through each character of the first string with this var
            char = strs[0][i]
            # now to check if the second string and so one has the same char
            for string in strs[1:]:
                # break condition to see the last common prefix
                # index of first string is bigger than the next string
                # or value of index in string is different than char
                if i >= len(string) or string[i] != char:
                    return prefix
            # if there are still common char, extend the prefix
            prefix += char
        return prefix

strs = ["flower","flow","flight"]
result = Solution()
result.longestCommonPrefix(strs)
print(result.longestCommonPrefix(strs))
