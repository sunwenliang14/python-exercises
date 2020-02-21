# 1.Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.
def is_two(n):
    if n == 2 or n == '2':
        return True
    else: return False

# 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
def is_vowel(i):
    if i.lower() in ('a','o','u','i','e'):
        return True
    else: return False
is_vowel('x')

# 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.
def is_consonant(i):
    if is_vowel(i):
        return False
    else: return True
is_consonant('b')

# 4.Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.
def string()