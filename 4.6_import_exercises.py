import function_exercises
function_exercises.is_two(n)

from function_exercises import is_vowel

from function_exercises import is_consonant as is_c

# 1.How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?

from itertools import product as p
combinations = list(p('abc', '123'))
combinations

# 2. How many different ways can you combine two of the letters from "abcd"?

from itertools import permutations as per
combs2 = list(per('abcd', 2))
combs2


from json import load
lis = load(open("profiles.json"))
lis

len(lis)

len([d for d in lis if d['isActive'] == True])

len([d for d in lis if d['isActive'] == False])

def handle_balance(s):
    return float(s[1:].replace(',', ''))
balances = [handle_balance(d['balance']) for d in lis]
total_balance = sum(balances)
total_balance


avg_balance = total_balance / len(lis)
avg_balance

user_with_lowest_balance = lis[0]
user_with_lowest_balance
for d in lis[1:]:
    if handle_balance(d['balance']) < handle_balance(user_with_lowest_balance['balance']):
        user_with_lowest_balance = d
user_with_lowest_balance

user_with_highest_balance = lis[0]
user_with_highest_balance
for d in lis[1:]:
    if handle_balance(d['balance']) > handle_balance(user_with_highest_balance['balance']):
        user_with_highest_balance = d
user_with_highest_balance

from collections import Counter
Counter([d['favoriteFruit'] for d in lis])

fruit_counts = {}
for d in lis:
    fruit = d['favoriteFruit']
    if fruit in fruit_counts:
        fruit_counts[fruit] += 1
    else:
        fruit_counts[fruit] = 1
fruit_counts'''


greetings = [d['greeting'] for d in lis]
greetings
res = list(map(lambda sub:int(''.join( 
      [ele for ele in sub if ele.isnumeric()])), greetings)) 
res
total = sum(i for i in res)
total