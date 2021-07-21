print('This program gives the LCM of numbers you choose.')
#This is the while loop to keep the program running continuously
while True:
    #This is the input prompt
    firstnumber = int(input('Type in a number '))
    secondnumber = int(input('Type in another number '))
    print('Calculating . . . Searching . . .')
    firstx = set()
    secondx = set()
    #This gives a huge variety of the multiples of the numbers put into the input(it goes up till 1,000,000)
    for i in range(1,1000001):
        firstx.add(firstnumber*i)
        secondx.add(secondnumber * i)

    #This finds a common value between both sets
    x = firstx.intersection(secondx)

    my_list = list(x)

    #This sorts the list full of common multiples
    my_list.sort()

    #This concatenates values in the program
    print('The LCM of (',firstnumber, ',',secondnumber,') is', my_list[0],'.')

    #This askes if you want to continue or not
    question = input('If you would like to exit the program, press the letter e. If you would like to continue the program, type CONTINUE! ')

    if question == 'CONTINUE':
        print('Okay! Let\'s continue!')

    elif question == 'e' or 'E':
        print('Bye! I hope you liked the program!')
        break
