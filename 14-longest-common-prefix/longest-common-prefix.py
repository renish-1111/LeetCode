class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        res = ""
        for i in range(len(strs[0])):
            for string in strs[1:]:
                if i < len(string) and string[i] == strs[0][i]:
                    None
                else:
                    return res
            res += strs[0][i]

        return res