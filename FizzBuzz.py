# Ben Woodfield
# Get your own solutions!
# Seriously this one wasn't that hard - if you need help with the game interface email me at raserppsprograms@gmail.com
# and I will talk you through the code and getting it to run in the game
# For now, heres a clue as to how it should be laid out...you have to do some of the work at least!

def checkio(cheater):
    if cheater % 5 == 0 and cheater % 3 == 0:
        print('This is basically the layout for the code')
    elif cheater % 3 == 0:
        print('Something else')
    elif cheater % 5 == 0:
        print('Something else again')
    else:
        print(cheater)
        
# you could check this code with:
# checater(15)
# or checkio(any_number)


'''
So what you want to do is write the function so the game (or anyonelse) can check it by using the command/code:
checkio(15) - or any other number. All you do is write the function to accept checkio(15) and the game handles
the rest. If you start the function off with checkio(number): exactly like it is already you will be fine
you just have to continue using the word number in the rest of the function/code

the function is already started on the games code editor/answer section it looks like this:
def checkio(number):

Be sure to keep this function name if you want compatability with the game (which you obviously do!)
Then you have to write the code inside that function. Go to the end of the function and hit enter 
to drop down to a new line in the right place (4 spaces from the left)

then you can start your code. the above example is basically right, but I wanted to make you do something
by yourself at least, so I changed the word 'number' for 'cheater' 

so you want it to say this:

FIRST LINE OF STATEMENT IN THE FUNCTION
Human: if the number is divisible by 5 and 3: print Fizz Buzz.
Python: if number % 5 == 0 and number % 3 == 0:
             print('Fizz Buzz')

The rest of the code is the same as this, except instead of "if" you use elif all the way until the very last
section where you use else to end the if/elif/else statement. It is just a case of saying: 

else if (elif) the number is divisible by 3: print Fizz
else if (elif) the number is divisible by 5: print Buzz
else: number is none of the above, just print 'number'


        
