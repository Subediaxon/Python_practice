from time import sleep
import numbers

print('''Collatz Sequence, or, the 3n + 1 Problem
By Al Sweigart al@inventwithpython.com
The Collatz sequence is a sequence of numbers produced from a starting
number n, following three rules:
 
1) If n is even, the next number n is n / 2.
2) If n is odd, the next number n is n * 3 + 1.
3) If n is 1, stop. Otherwise, repeat.
 
It is generally thought, but so far not mathematically proven, that
every starting number eventually terminates at 1.
''')
 
response = input('Enter a starting number (greater than 0) or QUIT:')

if (isinstance(response, numbers.Number)):
    if (response == 0):
        print('You must enter an integer greater than 0.')
    elif (response > 0):    
        while (response != 1):
            print(response, end="," )
            if (response%2==0):
                response = int(response/2)
                
            else:
                response = int((response * 3) + 1)
                #print(response, end=",");
                sleep(0.2);
    else:
        print("Thank you!!")
else:
    print("You did not enter a Number")
