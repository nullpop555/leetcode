class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        strs.sort(key=len)
        for i in range(len(strs[0])):
            for j in range(len(strs)):
                if strs[j][i] != strs[0][i]:
                    break
            else:
                ans = ans + strs[0][i]
                continue
            break
        return ans