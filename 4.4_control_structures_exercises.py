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

odd_number = input(Please input a number between 1 and 50)


