day_of_the_week = input('what day is today?')
if day_of_the_week.lower() == 'monday':
    print('Today is Monday!')
else:
    print('Today is not Monday!')


day_of_the_weekend = input('what day is today?')
if day_of_the_weekend.lower() == 'saturday' or day_of_the_weekend.lower()=='sunday':
    print('Today is Weekend!')
else:
    print('Today is Weekday!')


hours_worked = 8
hourly_rate = 50
weekly_paycheck = hours_worked * hourly_rate * 5
weekly_paycheck



-- 2. a Loop Basics
i = 5
while i <= 15:
    print(i)
    i += 1

n = 0
while n <= 100:
    print(n)
    n += 2

n = 100
while n >= -10:
    print(n)
    n -= 5

n = 2
while n <= 1000000:
    print(n)
    n = n**2

n = 100
while n >= 5:
    print(n)
    n -= 5

-- b.For Loops

num = input('please type a number')
num = int(num)
for n in range(1,11):
    print(f'{num} x {n} = {n * num}')
    

for n in range(1,10):
    print(str(n)*n)

