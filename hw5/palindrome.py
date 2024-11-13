def is_palindrome(text):
    processed_text = ""
    for char in text:
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
            processed_text += char.lower()

    # Reverse the processed text using slicing
    reversed_text = processed_text[::-1]

    return processed_text == reversed_text

print(is_palindrome("tacocat"))
print(is_palindrome("Tacocat"))
print(is_palindrome("Tacocat!"))
print(is_palindrome("A man, a plan, a canal, Panama"))