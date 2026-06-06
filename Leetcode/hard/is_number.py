



class Solution:
    def check_sign(self, s: str):
        sign = "-+"
        i = 0
        if s[i] in sign:
            i += 1
        while i < len(s) - 1:
            if s[i] in sign:
                print("here")
                if s[i - 1] in "eE":
                    i += 1
                else:
                    return False 
            i += 1
        return True

    def isNumber(self, s: str) -> bool:
        digits = "0123456789+-"
        sc_note = "e."
        if not self.check_sign(s):
            print("this1")
            return False
        for char in s:
            # print("character is : ", char)
            if char not in digits and char.lower() not in sc_note:
                print("this2")
                return False

            if char.lower() == "e":
                pos = s.index(char)
                if s[pos - 1] not in digits:
                    print("this3")
                    return False
                if s[pos + 1] not in digits and s[pos + 1] not in "+-":
                    return False
            
        return True
    
    
test = Solution()

number = "-3e3+7"


print(test.isNumber(number))
    
# txt = "hello world"

# p = txt.index("h")
# print(txt[p])
