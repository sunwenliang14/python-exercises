# a.Name the variable that holds the series fruits
import pandas as pd
fruits = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])

# b.Run .describe() on the series to see what describe returns for a series of strings.
fruits.describe

# c. Run the code necessary to produce only the unique fruit names.
fruits.unique()

#.d.Determine how many times each value occurs in the series.
fruits.value_counts()

# e.Determine the most frequently occurring fruit name from the series.
fruits.value_counts().head(1)

# f.Determine the least frequently occurring fruit name from the series.
fruits.value_counts().tail(11)

# g.Write the code to get the longest string from the fruits series.
max(fruits, key = len)

# h. Find the fruit(s) with 5 or more letters in the name.
fruits[fruits.str.len() > 5]

# i. Capitalize all the fruit strings in the series.
fruits.str.capitalize()

# j. Count the letter "a" in all the fruits (use string vectorization)
fruits.str.count('a').sum()

# k.Output the number of vowels in each and every fruit.
def number_of_vowels(s):  
    counter = 0
    for c in s.lower():
        if c in 'aouie':
            counter += 1
    return counter
fruits.apply(number_of_vowels)

# l.Use the .apply method and a lambda function to find the fruit(s) containing two or more "o" letters in the name.
fruits[fruits.apply(lambda s: s.count('o') >= 2)]

# m.Write the code to get only the fruits containing "berry" in the name
fruits[fruits.str.contains('berry')]

#. n.Write the code to get only the fruits containing "apple" in the name
fruits[fruits.str.contains('apple')]

# o. Which fruit has the highest amount of vowels?
fruits[fruits.apply(number_of_vowels).max()]

# 2. Use pandas to create a Series from the following data:What is the data type of the series? 
Object

# Use series operations to convert the series to a numeric data type
money = pd.Series(['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23'])
money = money.str.replace('[\$,]', '').astype('float')
money

# What is the maximum value? The minimum?
money.max()
money.min()

# Bin the data into 4 equally sized intervals and show how many values fall into each bin.
pd.cut(money, 4).value_counts()

# Plot a histogram of the data. Be sure to include a title and axis labels.
%matplotlib inline
import matplotlib.pyplot as plt
money.plot.hist()
plt.title('amount of money')

# 3 Use pandas to create a Series from the following exam scores:
scores = pd.Series([60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78])
scores.min()
scores.max()
scores.mean()
scores.median()

# Plot a histogram of the scores
scores.plot.hist()
plt.title('distribution of scores')


# Convert each of the numbers above into a letter grade. For example, 86 should be a 'B' and 95 should be an 'A'.

def grades(s):
    if s >= 90:
        return 'A'
    elif 80 <= s < 90:
        return 'B'
    elif 70 <= s < 80:
        return 'C'
    elif 60 <= s < 70:
        return 'D'
    else:
        return 'F'
scores.apply(grades)

# Write the code necessary to implement a curve. I.e. that grade closest to 100 should be converted to a 100, and that many points should be given to every other score as well.


# 4 Use pandas to create a Series from the following string:
string = pd.Series(list('hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'))
string.value_counts().sort_values()

# How many vowels are in the list?
string[string.apply(lambda x: x in 'aeiou')].count()

# How many consonants are in the list?
string[string.apply(lambda x: x not in 'aeiou')].count()



