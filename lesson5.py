import random
print('tack1:')
while True:
    rand = str(random.randint(1, 10))
    user_number = input('What number thought the computer?')
    if user_number.isdigit():
        if user_number == rand:
            print('You guessed!')
            break
        else:
            print('No! computer number :'+rand+'\nThe lottery is not yours!\nBut try again')
    else:
        print('Enter the number!')


print('tack2:')
while True:
    name = input('what\'s your name?:')
    if name.isalpha():
        age = int(input('How old are you?:'))
        print(f'Hello {name}!,on your next birthday you’ll be {age + 1} years')
        break

    else:
        print('What kind of "KOROVAN" !? I asked what your name is!')


print('tack3:')
my_string = input('Enter the string: ')
length = len(my_string)
number_of_lines = int(input('Enter number of lines: '))
new_string = ''
j = 0
while j < number_of_lines:
    index1 = random.randint(1, length)
    index2 = random.randint(1, length)
    step = 2
    if index1 != index2:
       new_string = my_string[index1:-index2] + my_string[-index1:index2]
    else:
        new_string = my_string[index1: -index2: step] + my_string[-index1: index2: step]
    j += 1
    print(new_string)

print('tack4:')
print('Simple tasks:')
num_1 = random.randint(0,10)
num_2 = random.randint(0,10)
while True:
    result = num_1+num_2
    print(f'{num_1} + {num_2} = ')
    result1 = int(input('Count! '))
    if result == result1:
        print('Right!')
    else:
        print('Wrong try again!')
        continue
    print(f'{num_1} - {num_2} = ')
    result = num_1 - num_2
    result1 = int(input('Count! '))
    if result == result1:
        print('Right!')
    else:
        print('Wrong try again!')
        continue
    print(f'{num_1} * {num_2} = ')
    result = num_1 * num_2
    result1 = int(input('Count! '))
    if result == result1:
        print('Right!')
    else:
        print('Wrong try again!')
        continue
    print(f'{num_1} / {num_2} = ')
    result = num_1 / num_2
    result1 = int(input('Count! '))
    if result == result1:
        print('Well done!')
        break
    else:
        print('Wrong try again!')
        continue