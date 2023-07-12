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
 
response = int(input('Enter a starting number (greater than 0) or QUIT:'))
try:
    
    if (response == 0):
        print('You must enter an integer greater than 0.')
    elif (response > 0):    
        print(response, end="," )  
        while (response != 1):
            if (response%2==0):
                response = int(response/2)
                #print(response, end="," )
            
            else:
                response = int((response * 3) + 1)
                sleep(0.2);
            print(response, end=",");
                
    else:
        print("Thank you!!")
except:
    print("You did not enter a Number")
