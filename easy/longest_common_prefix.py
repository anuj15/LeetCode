# https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        result = ""
        try:
            for i in range(len(strs[0])):
                y = set([x[i] for x in strs])
                if len(y) == 1:
                    result += list(y)[0]
                else:
                    break
        except Exception:
            pass
        return result


s = Solution()
r = s.longestCommonPrefix(["Flower", "flow", "flight"])
print(r)
r = s.longestCommonPrefix(["ccdogc", "ccracecarc", "cccarc"])
print(r)
r = s.longestCommonPrefix([""])
print(r)
r = s.longestCommonPrefix(["ab", "a"])
print(r)
r = s.longestCommonPrefix(["flower","flower","flower","flower"])
print(r)
