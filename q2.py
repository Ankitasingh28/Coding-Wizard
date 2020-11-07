import random

options = ["R" , "P", "S"]
AI = random.choice(options)
i = 0
u=0
c=0
while i < 3:
    user = input("Pick either R for Rock, P for Paper or S for Scissors: ")
    user = user.lower()
    if user == 'r' or 'p' or 's':
        print( "The computer has drawn %s whilst you have drawn %s " % (AI,user))

    if user == 'r':
        if AI == 'R':
            print ('Tie Game')
        elif AI == 'P':
            print('AI Wins')
            c+=1
        else:
            print('User Wins')
            u+=1
    elif user == 'p':
        if AI == 'R':
            print('User Wins')
            u+=1
        elif AI == 'P':
            print('Tie Game')
        else:
            print('AI Wins')
            c+=1
    elif user == 's':
        if AI == 'R':
            print('AI Wins')
            c+=1
        elif AI == 'P':
            print('User Wins')
            u+=1
        else:
            print('Tie Game')
    else:
        print('invalid output')
    i += 1
print('user score is '+str(u))
print ('computer score is '+str(c))
if u>c:
    print('user wins')
elif c>u:
    print('computer wins')
else:
    print ('game tied')