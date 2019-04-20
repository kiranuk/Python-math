def palindrome(str1):
    l = str1.lower()
    if l == l[::-1]:
        print("This is a palindrome")
    else:
        print("This is not a palindrome")

palindrome("Malayalam")
palindrome("malayalam")
