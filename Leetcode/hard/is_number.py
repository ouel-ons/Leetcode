



class Solution:
    def check_sign(self, s: str):
        sign = "-+"
        i = 0
        if s[i] in sign:
            i += 1
        while i < len(s) - 1:
            if s[i] in sign:
                if s[i - 1] in "eE":
                    i += 1
                else:
                    return False 
            i += 1
        return True
    def check_dot(self, s):
        count = 0
        for i in s:
            if i == ".":
                count += 1
        if count > 1:
            return False
        d = "0123456789"
        try:
            if "." in s and len(s) >= 3:
                pos = s.index(".")
                if s[pos - 1] not in d or s[pos + 1] not in d:
                    return False
        except IndexError:
            return False
        return not count == len(s)

    def isNumber(self, s: str) -> bool:
        digits = "0123456789+-"
        sc_note = "e."
        if not self.check_sign(s):
            return False
        if not self.check_dot(s):
            return False

        for char in s:
            if char not in digits and char.lower() not in sc_note:
                return False
            try:
                if char.lower() == "e":
                    pos = s.index(char)
                    if s[0] in "Ee":
                        return False
                    if "." in s:
                        pts = s.index(".")
                        if pts > pos:
                            return False
                    if s[pos - 1] not in digits:
                        return False
                    if s[pos + 1] not in digits and s[pos + 1] not in "+-":
                        return False
            except:
                return False
            
        return True
    
    
test = Solution()

number = ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]
# "2e10", "-90E3", "3e+7", "+6e-1"

# for i in number:
#     print(test.isNumber(i))
    

n = "3."
print(test.isNumber(n))
# txt = "hello world"

# p = txt.index("h")
# print(txt[p])
