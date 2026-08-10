# Strings & Formatting Examples and Practice

# 1. Immutability Demonstration
original = "hello"
modified = original.replace('h', 'H')
print(f"Original: {original}, Modified: {modified}")

# 2. String methods demo
raw_input = "   apple, banana, cherry   "
clean_list = [x.strip() for x in raw_input.split(',')]
print("Clean List:", clean_list)

joined_str = " | ".join(clean_list)
print("Joined String:", joined_str)

# 3. Formatting with f-strings
pi_val = 3.14159265
print(f"Pi to 3 decimal places: {pi_val:.3f}")

# Practice: Check if string is palindrome
def is_palindrome(text):
    clean_text = "".join(char.lower() for char in text if char.isalnum())
    return clean_text == clean_text[::-1]

print("Is 'A man, a plan, a canal: Panama' a palindrome?", is_palindrome("A man, a plan, a canal: Panama"))
