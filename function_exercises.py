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
def string(s):
    if s[0] in ('a','o','u','i','e'):
        return s.capitalize()
    else:
        return s

# 5.Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

def calculate_tip(percentage, bill_amount):
    tip_amount = percentage * bill_amount
    return tip_amount

# 6. Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied

def apply_discount(original_price, discount):
    amount_after_discount = original_price - original_price * discount
    return amount_after_discount


# 7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.

def handle_commas(s):
    s = s.replace(',', '')
    return int(s)

# 8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F)

def get_letter_grade(n):
    if n >= 90:
        return 'A'
    elif n >= 80:
        return 'B'
    elif n >= 70:
        return 'C'
    elif n >= 60:
        return 'D'
    else:
        return 'F'
    
# 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

def remove_vowels(s):
    words = list(s)
    v = ["a", "e", "i", "o", "u"]   
    return "".join([i for i in words if i.lower() not in v])

# 10. 

def remove_special_characters(string):
    return ''.join([c for c in string if c.isalnum() or c == ' '])

def normalize_name(string):
    without_special_chars = remove_special_characters(string)
    return without_special_chars.lower().strip().replace(' ', '_')

# 11

def cumsum(numbers):
    total = 0
    cumulative_sums = []
    for n in numbers:
        total += n
        cumulative_sums.append(total)
    return cumulative_sums

# 1.Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm and return a string that is the representation of the time in a 24-hour format. Bonus write a function that does the opposite

def twelveto24(str1): 
    if str1[-2:] == "AM" and str1[:2] == "12":
        return "00" + str1[2:-2] 
    elif str1[-2:] == "AM": 
        return str1[:-2] 
    elif str1[-2:] == "PM" and str1[:2] == "12": 
        return str1[:-2] 
    else: 
        return str(int(str1[:2]) + 12) + str1[2:5]

