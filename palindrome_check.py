def palindrome_check(s1):
    palindrome = False
    s2 = s1[::-1]
    if s1 == s2:
        palindrome = True
    return palindrome
