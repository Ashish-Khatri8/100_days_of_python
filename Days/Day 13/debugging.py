# Day 13 project - Debugging.

############ Bugged code examples. ############
# Uncomment each problem one by one and then debug them all.

# 1
#def my_function():
#    for i in range(1, 20):
#        if i == 20:
#            print("You got it")
#my_function()

# 2
#from random import randint
#dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
#dice_num = randint(1, 6)
#print(dice_imgs[dice_num])

# 3
#year = int(input("What's your year of birth?"))
#if year > 1980 and year < 1994:
#    print("You are a millenial.")
#elif year > 1994:
#    print("You are a Gen Z.")

# 4
#age = input("How old are you?")
#if age > 18:
#    print("You can drive at age {age}.")

# 5
#pages = 0
#word_per_page = 0
#pages = int(input("Number of pages: "))
#word_per_page == int(input("Number of words per page: "))
#total_words = pages * word_per_page
#print(total_words)

# 6
#def mutate(a_list):
#    b_list = []
#    for item in a_list:
#        new_item = item * 2
#    b_list.append(new_item)
#    print(b_list)
#mutate([1,2,3,5,8,13])

# 7
#number = int(input("Which number do you want to check?"))
#if number % 2 = 0:
#    print("This is an even number.")
#else:
#    print("This is an odd number.")

# 8
#year = input("Which year do you want to check?")
#if year % 4 == 0:
#    if year % 100 == 0:
#        if year % 400 == 0:
#            print("Leap year.")
#        else:
#            print("Not leap year.")
#    else:
#        prirnt("Leap year.")
#else:
#    print("Not leap year.")

# 9
#for number in range(1, 101):
#    if number % 3 == 0 or number % 5 == 0:
#        print("FizzBuzz")
#    if number % 3 == 0:
#        print("Fizz")
#    if number % 5 == 0:
#        print("Buzz")
#    else:
#        print([number])


############ Debugged code solutions. ############

# 1
#def my_function():
#    for i in range(1, 21):   # range(x, y) , y is not included.
#        if i == 20:
#            print("You got it")
#my_function()

# 2
#from random import randint
#dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
#dice_num = randint(0, 5)    # list index starts from 0.
#print(dice_imgs[dice_num])

# 3
#year = int(input("What's your year of birth?"))
#if year > 1980 and year < 1994:
#    print("You are a millenial.")
#elif year >= 1994:                 # 1994 was not being checked.
#    print("You are a Gen Z.")

# 4
#age = int(input("How old are you?"))  # Take age input as integer.
#if age > 18:
#    print(f"You can drive at age {age}.")    # f-string

# 5
#pages = 0
#word_per_page = 0
#pages = int(input("Number of pages: "))
## == is used for checking equality
#word_per_page = int(input("Number of words per page: ")) 
#total_words = pages * word_per_page
#print(total_words)

# 6
#def mutate(a_list):
#    b_list = []
#    for item in a_list:
#        new_item = item * 2
#        b_list.append(new_item)       # Improper indentation
#    print(b_list)
#mutate([1,2,3,5,8,13])

# 7
#number = int(input("Which number do you want to check?"))
#if number % 2 == 0:      # = is assignment operator. == is used to check equality.
#    print("This is an even number.")
#else:
#    print("This is an odd number.")

# 8
#year = int(input("Which year do you want to check?")) # take year input as integer
#if year % 4 == 0:
#    if year % 100 == 0:
#        if year % 400 == 0:
#            print("Leap year.")
#        else:
#            print("Not leap year.")
#    else:
#        prirnt("Leap year.")
#else:
#    print("Not leap year.")

# 9
#for number in range(1, 101):
#    if number % 3 == 0 and number % 5 == 0:  # and will be used.
#        print("FizzBuzz")
#    elif number % 3 == 0:     # elif block
#        print("Fizz")
#    elif number % 5 == 0:     #elif block
#        print("Buzz")
#    else:
#        print(number)       # number is not a list.
