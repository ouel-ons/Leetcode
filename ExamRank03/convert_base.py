


def convert_base(num: str, from_base: int, to_base: int) -> str:
    try :
        base = "0123456789ABCDEFGHIJKLMNOPKRSTUVWXYZ"
        if not 2 <= from_base <= 36:
            return "ERROR"
        if not 2 <= to_base <= 36:
            return "ERROR"
        n = int(num, from_base)
        if n == 0:
            return "0"
        res = ""
        while n:
            res += base[n % to_base]
            n //= to_base
        return res[::-1]
    except Exception:
        return "ERROR"
    
# Basic conversions
convert_base("1010", 2, 10)        # "10"
convert_base("10", 10, 2)          # "1010"
convert_base("1A", 16, 10)         # "26"
convert_base("26", 10, 16)         # "1A"

# Same base
convert_base("123", 10, 10)        # "123"

# Edge cases
convert_base("0", 10, 2)           # "0"
convert_base("000", 2, 10)         # "0"

# Larger bases
convert_base("ZZZ", 36, 10)        # "46655"
convert_base("46655", 10, 36)      # "ZZZ"

# Uppercase handling
convert_base("A", 16, 10)          # "10"
convert_base("F", 16, 10)          # "15"

# Mixed digits and letters
convert_base("1F4", 16, 10)        # "500"
convert_base("500", 10, 16)        # "1F4"

# Invalid cases 
convert_base("2", 2, 10)           # Error / invalid input
convert_base("G", 16, 10)       # Error / invalid input