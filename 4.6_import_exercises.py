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