def is_palindrome(word):
    # Convert the word to lowercase to make the comparison case-insensitive
    word = word.lower()
    
    # Check if the word is equal to its reverse
    return word == word[::-1]

# Example usage:
test_word = "radar"
result = is_palindrome(test_word)

if result:
    print(f"The word '{test_word}' is a palindrome.")
else:
    print(f"The word '{test_word}' is not a palindrome.")


