class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) <= 1:
            return False
        m = s[1::2]
        n = s[::2]
        print(n)
        d = {"(":")", "{":"}", "[":"]"}
        try:
            for i, j in enumerate(n):
                print(i, j, d[j], m[i])
                if d[j] != m[i]:
                    return False
            return True

        except KeyError:
            return False


a = "{}{}(}()()"
print(Solution().isValid(a))