#A program that keeps asking for a password until it is valid. 
#Password is “helloworld”
######Answer
password = "helloworld"
user_input=""
while user_input != password:
    user_input=input("Input password: ")
print("out of while")

#   Ask user for 5 students’ grades and check if they passed or not. 
#   Passing grade is 70
# 1
for student in range (5):
    grade = int(input("Introduce grade"))
    if grade >= 70:
        print("You passed")
    else:
        print("you did not pass")
print("out of the for")
# 2
grades=list()
for student in range(5):
    grade = int(input("Introduce grade"))
    grades.append(grade)
for grade in grades:
    if grade >= 70:
        print("You passed")
    else:
        print("you did not pass")
print("out of the while")

#Create a logging system that only allows 3 attepmts at a wrong password/user to enter
#Define password and user yourself

password = "1234"
user = "fedragl"
attempt_limit = 3
attempts = 1
user_input =""
password_inpt = ""
while (user_input!= user or password_inpt!= password)and (attempts <= attempt_limit):
    user_input = input("Introduce user: ")
    password_inpt = input("Introduce password: ")

    if (password_inpt == password) and (user_input == user):
        print("You logged in") 