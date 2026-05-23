def is_palindrome(s):
    c = ""
    # Remove non-alphanumeric characters and convert to lowercase
    for char in s:
        if char.isalnum():
            c += char.lower()

    return c == c[::-1]


print(is_palindrome("A man a plan a canal Panama"))  
print(is_palindrome("racecar"))                      
print(is_palindrome("Hello"))                        
print(is_palindrome("No lemon, no melon"))           
print(is_palindrome(""))                             