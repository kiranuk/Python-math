"""This function is to check if string is a palindrome or not.
If string is not a palindrome, then it will return the palindrome version.
Also  will return count how many letters added to make palindrome"""


def make_palindrome(str1):
    s = str1.lower()
    r = s[::-1]
    if s == r:
        return "This is already a palindrome"
    else:
        res = s[:] + r[1:]
        count = int(len(res)/2)
        return res, count


print(make_palindrome("Malayalam"))
print(make_palindrome("Hello"))
print(make_palindrome("helloworld"))
