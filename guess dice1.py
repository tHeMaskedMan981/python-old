import os, random



def playAgain ():

    print ' Want to play more (y/n)?' 
    c=raw_input().lower().startswith('y')
    return c

while True:
    print ' guesss a no from 1-6 :'
    b= int(raw_input())
    a=random.randint(1,6)

    if a==b :
        print 'u guessed it right..!! U WIN..!!'
    else :
        print ' oops.. wrong guess \n'
    if not playAgain():
        break





