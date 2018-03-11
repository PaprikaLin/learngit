class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        for i, j in enumerate(zip(*strs)):
            if len(set(j)) > 1:
                return strs[0][:i]

        return min(strs)

strs = ['baa', 'ava', "a"]
a = Solution()
print(a.longestCommonPrefix(['baa', 'ava', ""]))
print(min(strs))