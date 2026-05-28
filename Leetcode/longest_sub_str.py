

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = ""
        sub = []
        stack = []
        if len(s) == 1:
            return 1
        i = 0
        while i < len(s):
            
            if s[i] in stack:
                sub.append(res)
                res = s[i]
                i += 1
                continue
            stack.append(s[i])
            res += s[i]
            i += 1
        sub.append(res)
        sub = sorted(sub, key=lambda x: len(x))
        print(sub)
        if len(sub) == 0:
            return 0
        p = sub.pop()
        return len(p)


c = Solution()


s = "dvdf"
print(c.lengthOfLongestSubstring(s))