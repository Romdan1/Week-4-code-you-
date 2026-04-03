
def is_palindrome(name):
    name = name.lower().replace(" ", "")
    
    # Reverse the string
    reversed_name = name[::-1]
    
    # Compare and return True or False
    if name == reversed_name:
        return True
    else:
        return False
print(is_palindrome("racecar"))   # True
print(is_palindrome("hello"))     # False
print(is_palindrome("Race Car"))  # True