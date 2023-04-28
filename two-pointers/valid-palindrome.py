# Resursive Solution

def isPalindromeRecursive(string):
    if len(string) == 0 or len(string) == 0:
        return True
    if string[0] != string[-1]:
        return False
    return isPalindromeRecursive(string[1:-1])


print(isPalindromeRecursive('raceca'))
print(isPalindromeRecursive('raceca'))
