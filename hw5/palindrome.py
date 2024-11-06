def is_palindrome(string_in):
    # The function works by comparing pairs of characters at the 'start' and
    # 'end' index. At first, 'start' is index 0 (the start of the string), and
    # 'end' is the last character in the string.
    modified_string = ''.join([char for char in string_in if char.isalpha()])
    modified_string = modified_string.lower()
    start = 0 
    end = len(modified_string) - 1

    is_palindrome = True    # Assume a palindrome unless we discover otherwise in the loop

    # If we reach a point where start > end, then we have checked all pairs of characters
    # in the string and can stop.
    while start <= end:
        if (modified_string[start] != modified_string[end]):
            # If the characters are not equal, the string cannot be a palindrome.
            # Set is_palindrome appropriately and exit the loop
            is_palindrome = False
            break
        
        # If we reach this point, the characters are equal. We can continue looking -
        # move start forward and end backward, then loop again.
        start = start + 1
        end = end - 1
        
    return is_palindrome

print(is_palindrome("tacocat"))
print(is_palindrome("Tacocat!"))
print(is_palindrome("A man, a plan, a canal: Panama"))