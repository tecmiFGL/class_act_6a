#A program that keeps asking for a password until it is valid. 
#Password is “helloworld”
"""password = "helloworld"
user_input = ""

while password != user_input: #condition(has to be true):
    user_input = input("Introduce password ")"""

"""for i in range (5):
    grade = int(input("student grades"))    # user input
    if grade >= 70:
        print("Student passed")
    else:
        print("Student did not pass")"""

"""grades =list()
for i in range(5):
    grade = int(input("student grades")) 
    grades.append(grade)
for grade in grades:
    if grade >= 70:
        print("Student passed")
    else:
        print("Student did not pass")"""
        
password = "1234"
user = "fedragl"
user_input=""
password_input=""
attempts=1
limit = 3
# as long as attempts <= limit, ask for user input
while (attempts <= limit):
    user_input=input("introduce user")
    password_input=input("introduce password")
    attempts+=1
    if (password==password_input) and (user== user_input):
        print("Correct credentials")
        attempts= 4
print("out of while")