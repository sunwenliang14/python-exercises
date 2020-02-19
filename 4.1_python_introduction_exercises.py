print('Hello, World')
greeting = 'hello curie'
print(greeting)

[ x * 2 for x in range(10) if x > 5]

[x /2 for x in range(10) if x % 2 != 0]

[ x + 3 for x in range(10) if x % 2 =0 and x < 7]

movies = {'The little mermaid': 3, 'Brother Bear':5, 'Hercules':1 'price':3}


username = 'codeup'
password = 'notastrongpassword'

""" Create a variable that holds a boolean value for each of the following conditions:

the password must be at least 5 characters
the username must be no more than 20 characters
the password must not be the same as the username
bonus neither the username or password can start or end with whitespace"""

[length_of_passowrd for length_of_passowrd in password if len(password) >= 5]

[length_of_username for length_of_username in username if len(username) =< 20]

[for_password for for_password in password if password != username

[username is not start with ' ' and password is not start with ' ']