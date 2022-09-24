

from math import nan


def add_two(num1, num2):
    add_result = float(num1) + float(num2)
    return add_result

# try:
#     user_selected = input("select the operator", '1. add', '2. subtract', '3. mul')
#     if (user_selected == 1):
#         num1_input = input('enter your first number:')  
# except:


print('Welcome, this is a simple calculator. ', "here are the options")
print('1. addition')
print('2. subtraction')
print('3. multiplication')
print('4. division')


while True:
    try:
        user_selected = int(input('choose, and enter the number: '))
        if(user_selected < 0 or user_selected > 5):
            print("that's outside the range")
        else:
            break
    except ValueError:
        print('you fat fingered something, try again')
print(user_selected)


# user_selected = int(input('choose, and enter the number: '))
