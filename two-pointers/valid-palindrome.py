# Resursive Solution

def isPalindromeRecursive(string):
    if len(string) == 0 or len(string) == 0:
        return True
    if string[0] != string[-1]:
        return False
    return isPalindromeRecursive(string[1:-1])


# print(isPalindromeRecursive('raceca'))
# print(isPalindromeRecursive('raceca'))

def isPalindrome(string):
    left, right = 0, len(string) - 1

    while left < right:

        if string[left] != string[right]:
            return False

        left += 1
        right -= 1

    return True


print(isPalindrome("racca"))
print(isPalindrome("racecar"))
