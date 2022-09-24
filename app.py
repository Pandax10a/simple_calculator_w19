

from math import nan

# 4 functions here for the 4 math operations
def add_two(num1, num2):
    add_result = float(num1) + float(num2)
    return add_result

def subtraction_of_two(num1, num2):
    the_result = float(num1) - float(num2)
    return the_result

def multiplication_two(num1, num2):
    the_result = float(num1) * float(num2)
    return the_result

def division_two(num1, num2):
    if(num1 == 0 and num2 == 0):
        return 0
    else:
        the_result = float(num1) / float(num2)
        return the_result


print('Welcome, this is a simple calculator. ', "here are the options")
print('1. addition')
print('2. subtraction')
print('3. multiplication')
print('4. division')

# using while and set to true so it will run the try infinite number of times
while True:
    try:
        user_selected = int(input('choose, and enter the number: '))
        if(user_selected < 0 or user_selected > 5):
            print("that's outside the range")
        else:
            # the break here is if the try no longer has ValueError problem so it breaks out of the while loop
            break
    except ValueError:
        print('you fat fingered something, try again')
print(user_selected)


stored_input = []

while True:
    try:
        num1 = float(input('enter the first number: '))
        # conditions when division is selected
        if(user_selected == 4):
            # if first number is 0, function was having a fit
            if(num1 == 0):
                num2 = float(input('enter the second number and it can be 0: '))
            else:
                num2 = float(input('enter the second number and it can not be 0: '))
                # condition for dividing things by 0, it will change the value to force it to ValueError
                if(num2 == 0):
                    num2 = 'error'
                    print('this number can not be zero')
                    float(num2)
        else:
            num2 = float(input('enter the second number: '))
            
        stored_input.append(num1)
        stored_input.append(num2)
            
          
        break
    except ValueError:
        print('both needs to be a numeric value for operation 1 to 3, and second number can not be zero for division, try again')

# have to copy and paste seperate rule for division

            
          
        
    except ValueError:
        print('both needs to be a numeric value, try again')
# try to make it more compact with conditionals in using the def
if (user_selected == 1):
    print('the result: ', add_two(stored_input[0], stored_input[1]))
elif (user_selected == 2):
    print('the result: ', subtraction_of_two(stored_input[0], stored_input[1]))
elif (user_selected == 3):
    print('the result: ', multiplication_two(stored_input[0], stored_input[1]))
elif (user_selected == 4):
    print('the result: ', division_two(stored_input[0], stored_input[1]))

# for my reference
print(stored_input)


# user_selected = int(input('choose, and enter the number: '))
