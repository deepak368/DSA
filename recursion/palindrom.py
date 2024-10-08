def palindrom(i):
    if i >= n/2:
        return True
    if s[i] != s[n-i-1]:
        return False
    return palindrom(i + 1)

s = 'malayalam'
n = len(s)
print(palindrom(0))