def is_palindrome(value):
    value_str = str(value)
    return value_str == value_str[::-1]

# Test examples
print(is_palindrome(121))       
print(is_palindrome(123))       
print(is_palindrome("radar"))   
print(is_palindrome("hello"))   
