# range is 1 - 101
# when number % 3 == 0 then fizz
# when number % 5 == 0 then buzz
# when number % 3 == 0 and number % 5  == 0 then fizz buzz

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print('FizzBuzz')
    elif number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        print(number)
