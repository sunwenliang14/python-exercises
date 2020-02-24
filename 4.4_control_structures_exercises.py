day_of_the_week = input('what day is it today?')
if day_of_the_week.lower() == 'monday':
    print('Today is Monday!')
else:
    print(f''Today is not Monday! It's {day_of_the_week.capitalize()}'')


day = input('what day is today?')
if day.lower() == 'saturday' or day.lower()=='sunday':
     print(f"{day.capitalize()} is a weekend!")
else:
    print(f"{day.capitalize()} is a weekday day!")


hours_worked = 52
hourly_rate = 40

if hours_worked <= 40:
    total = hourly_rate * hours_worked
else:
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * 1.5 * hourly_rate
    regular_pay = 40 * hourly_rate
    total = regular_pay + overtime_pay

print(f"Total pay is ${total}")



-- 2. a Loop Basics
i = 5
while i <= 15:
    print(i)
    i += 1

i = 0
while i <= 100:
    print(i)
    i += 2

i = 100
while i >= -10:
    print(i)
    i -= 5

i = 2
while i <= 1000000:
    print(i)
    i *= i

i = 100
while i >= 5:
    print(i)
    i -= 5

-- b.For Loops

num = input('please input a number')
num = int(num)
for i in range(1,11):
    print(f'{num} x {i} = {num * i}')
    

for i in range(1,10):
    print(str(i)*i)


user_choise = input('please input a odd number between 1 and 50 ')
while  user_choise.isdigit() == False or int(user_choise) > 50 or int(user_choise) < 1 or int(user_choise) % 2 ==0:
    user_choise = input('please input a odd number between 1 and 50 ')
user_choise = int(user_choise)
for i in range(1,50):
    if i % 2 == 0:
        continue
    elif i == user_choise :
        print(f"Skipping {i}")
    else:
        print(f"{i} is an odd number.")


user_choice = input('Please input a positive number')
while (user_choice.isdigit() == False  
            or int(user_choice) <= 0):   
    print(f"{user_choice} is awesome, but we need a positive number.")
    user_choice = input("Please input a positive number")

user_choice = int(user_choice)
for i in range(user_choice + 1):
    print(i)

user_choice = input('Please input a positive number')
user_choice = int(user_choice)
while user_choice >= 1:
    print(user_choice)
    user_choice -= 1


for i in range(1,101):

    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 5 == 0:
        print('Buzz')
    elif i % 3 == 0:
        print('Fizz')
    else:
        print(i)
        

def get_positive_number():
    user_choice = input("Please input a positive number ")
    while (user_choice.isdigit() == False  
            or int(user_choice) < 1):   
        print(f"{user_choice} is nice, but we'll need a positive number.")
        user_choice = input("Please input a positive number")

    user_choice = int(user_choice)
    return user_choice

choice = "yes"
while choice in ["y", "yes"]:
    user_choice = get_positive_number()
    print(" number | squared | cubed ")
    for i in range(1, user_choice + 1):
        print(f"{i}    |   {i**2}    |   {i**3} ")
    
    
    choice = input("Do you want to continue? Type Y or Yes")
    choice = choice.lower()

print("Thank you!")


while True:
    user_choice = input('please input a numerical number between 0 and 100')
    user_choice = int(user_choice)
    if  88 <= user_choice:
            print(f"{user_choice} is an A")
    elif 80 <= user_choice:
            print(f"{user_choice} is an B")
    elif 67 <= user_choice:
             print(f"{user_choice} is an C")
    elif 60 <= user_choice:
            print(f"{user_choice} is an D")
    else:
        print(f"{user_choice} is an F")
    user_choice = input("Do you want to continue? Type y or Yes. ")
    if user_choice.lower() in ["y", "yes"]:
        continue
    else:
        print('Thank you!')
        break


    books = [
    {
        "title": "Visual Display of Quantitative Information",
        "author": "Edward Tufte",
        "genre": "visualization"
    },
    {
        "title": "Deep Learning with Python",
        "author": "Fracois Challot",
        "genre": "deep learning"
    },
    {
        "title": "How Charts Lie",
        "author": "Cario",
        "genre": "visualization"
    },
]

for book in books:
    print(f"'{book['title']}' by {book['author']} is about {book['genre']}")
