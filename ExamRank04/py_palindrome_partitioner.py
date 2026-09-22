def palindrome_partitioner(s: str) -> int:
    n = len(s)
    if n <= 1:
        return 0
    
    # is_pal[i][j] = True if s[i:j+1] is a palindrome
    # Build it with a 2D list
    is_pal = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(False)
        is_pal.append(row)
    
    # Fill the palindrome table
    for i in range(n):
        is_pal[i][i] = True          # single char is a palindrome
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            is_pal[i][i + 1] = True  # two equal chars
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and is_pal[i + 1][j - 1]:
                is_pal[i][j] = True
    
    # cuts[i] = min cuts for s[0:i+1]
    cuts = []
    for i in range(n):
        cuts.append(i)  # worst case: cut every char
    
    for i in range(n):
        if is_pal[0][i]:
            cuts[i] = 0
            continue
        for j in range(i):
            if is_pal[j + 1][i]:
                if cuts[j] + 1 < cuts[i]:
                    cuts[i] = cuts[j] + 1
    
    return cuts[n - 1]