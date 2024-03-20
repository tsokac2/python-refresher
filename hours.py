# print("Hello World")

# DATE AND TIME
# import datetime
# nowDate = datetime.datetime.now()
# print(f"At the moment is {nowDate}")

# VARIABLES
# mynumber = 10
# mytext = "Hello"
# print(mynumber, mytext)


# SIMPLE TYPES
# x = 10
# y = "10"
# z = 10.1

# sum1 = x + x
# sum2 = y + y

# print(sum1, sum2)
# print(f"X variable is {type(x)}")
# print(f"Y variable is {type(y)}")
# print(f"Z variable is {type(z)}")

# LIST TYPES
# student_grades = [9.1, 8.8, 7.5]
# print(f"The data type of student_grades is {type(student_grades)}")
# print(f"These are studens grades: {student_grades}")

# ATTRIBUTES writing in the shell
# in the console write:
# dir(int)
# dir(float)
# dir(lists)
# dir(str)

# CALCULAT AVARAGE
# student_grades = [9.1, 8.8, 7.5]
# mysum = sum(student_grades)
# length = len(student_grades)
# res = mysum/length
# print(res)


# DICTONARY TYPES
# monday_temperature = [9.1, 8.8, 7.5]
# studen_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}

# print(studen_grades.values())
# print(studen_grades.keys())

# mysum = sum(studen_grades.values())
# length = len(studen_grades)
# res = mysum/length
# print(res)

# TUPLE TYPES
# monday_temperatures = (1,4,5) # Tuple is imutable
# monday_temperatures2 = [1,2,3] # List is mutable - you can add values dynamicly
# # monday_temperatures.append(4) # error will not work
# monday_temperatures2.append(4)
# monday_temperatures2.remove(1)
# print(monday_temperatures2)

# COMAND LINE TIPS
# Clear the screen: clear, cls, CTRL + l


# OPERATIONS WITH LISTS
# monday_temperatures = [9.1, 8.8, 8.8, 7.5]
# monday_temperatures.append(8.1) # appean - add new element to the list
# print(monday_temperatures.index(8.8))
# print(monday_temperatures.count(8.8))
# print(monday_temperatures)


# LIST INDEXING
# monday_temperatures = [9.1, 8.8, 8.8, 7.5]
# res = monday_temperatures.__getitem__(1) # Getitem method
# print(res)
# print(monday_temperatures[1])


# LIST SLICING
# monday_temperatures = [9.1, 8.8, 8.8, 7.5, 9.9]
# print(len(monday_temperatures)) # returns 5
# print(monday_temperatures[0:2]) # returns [9.1, 8.8]
# print(monday_temperatures[:2]) # returns [9.1, 8.8]
# print(monday_temperatures[3:]) # returns [7.5, 9.9]


# ACCESSING ITMES AND SLICES WITH NEGATIVE INDEXES
# monday_temperatures = [9.1, 8.8, 8.8, 7.5, 9.9]
# print(monday_temperatures[-1]) # Returns 9.9
# print(monday_temperatures[-5]) # Returns 9.1
# print(monday_temperatures[-2:]) # Returns [7.5, 9.9]
# print(monday_temperatures[-4:-2]) # Returns [8.8, 8.8]
# print(monday_temperatures[-5:1]) # Returns [9.1]


# ACCESSING CHARACTERS AND SLICEC IN STRINGS
# myString = "Hello World"
# print(myString[3:]) # Returns "lo World"
# myItmes = ["hello", 1, 2, 3]
# print(myItmes[0][2]) # Returns l


# ACCESSING ITEMS IN DICTIONARIES
# studnts_grades = {
#     "Marry": 9.1,
#     "Sim": 8.8,
#     "John": 7.5
# }
# print(studnts_grades["Sim"])


# CREATING FUNCTIONS
# def avaregFunc(myList):
#     the_mean = sum(myList)/len(myList)
#     return print(the_mean)
# listUser = [1,4,6]
# avaregFunc(listUser) # Returns: 3.6666666666666665
# print(type(avaregFunc), type(sum)) # Returns: <class 'function'> <class 'builtin_function_or_method'>


# PRINT OR RETURN
# def printOrReturn(myList):
#     print("Function started!")
#     the_mean = sum(myList) / len(myList)
#     return the_mean

# mymean = printOrReturn([0,3,4])
# print(mymean + 10)
# print(printOrReturn([1,2,3])) # Returns 2.0 and None - since return keyword is not define


# CONDITIONALS - "if", 
# def mean(value):
#     print("Function has started")
#     if type(value) == dict: # Cheking the type of dictonary
#         the_mean = sum(value.values()) / len(value)
#     else:
#         the_mean = sum(value) / len(value)
#     return the_mean

# moday_temperatures = [8.8, 10, 21]
# student_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}
# print(mean(moday_temperatures))
# print(mean(student_grades))

# Outsideblock
# if 3 > 1:
#     print("Greater")
# else:
#     print("Not Greater")

# ELIF CONDITIONALS
# x = 3
# y = 1
# if x > y:
#     print("x is greater than y")
# elif x == y:
#     print("x is equeal to y")
# else:
#     print("x is less that y")

# WHITE SPACE
# if 3 > 1:
#     print("a")
# print("aa")
# print("aaa")

# if 3>               1:
#     print("b")
# print("bb")
# print("bbb")

# if 3 > 1:
#     print("c")
# print("cc")
# print("ccc")

# USER INPUT
# def weather_condition(temp):
#     if temp > 7:
#         return "Warm"
#     else:
#         return "Cold"

# user_input = float(input("Enter Temperature:")) # by default the user_input will be string
# # print(user_input.lower())
# print(weather_condition(user_input))

# user_input = int(input("Enter a value:"))
# user_input = input("Enter a value:")
# print(type(user_input))

# STRING FORMATING
# user_input = input("Enter your name: ")
# # message = "Hello %s!" % user_input
# message = f"Hello {user_input}"
# print(message) # Returns "Hello <what ever you enter>"

# STRING FORMATING WITH MULTIPLE VARIABLES
# name = input("Enter your name: ")
# sname = input("Enter your name: ")
# # message = "Hello %s %s" % (name, sname)
# message = f"Hello {name} {sname}" # Returns "Hello <what ever you enter for "name" and "sname">"
# print(message)

# FOR LOOPS - HOW AND WHY
# monday_temperatures = [9.1, 8.8, 7.6]

# for temp in monday_temperatures:
#     print(round(temp))
#     print("DONE")

# for letter in "hello":
#     print(letter)
#     print("DONE")

# for letter in "tomislav":
#     print(letter.title())

# LOOPING THROUG DICTONARY
# student_grades = {"Marry":9.1, "Sim": 8.8, "John": 7.5}

# for grades in student_grades.keys(): # prints "Marry", "Sim", "John"
#     print(grades)

# for grades in student_grades.values(): # prints 9.1,8.8,7.5
#     print(grades)

# WHILE LOOP EXAMPLE WITH OUTPUT
# username = ''
# while username != "Tom":
#     username = input("Enter username: ")

# WHILE LOOPS - HOW AND WHY
# for i in [1,2,3]:
#     print(i)

# a = 3

# while a > 0:
#     print(1)
#     print(2)

# username = ''

# while username != 'tom':
#     username = input("Enter username: ")


# Using break 
# while True:
#     username = input("Enter username: ")
#     if username == "tom":
#         print(f"Hello {username}") #  Returns "tom" when the condition is true
#         break
#     else:
#         continue

# HOW THE OUTPU LOOKS LIKE






