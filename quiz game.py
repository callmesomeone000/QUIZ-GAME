print('Welcome to the quiz game')
playing=input('Do you want to play the game? ')

if playing.lower() != 'yes':
    quit()

print('Okay! So lets play!')

score=0

answer=input('What is the full form of GPU? ')
if answer.lower() == 'graphics processing unit' :
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer=input('What is the full form of RAM? ')
if answer.lower() == 'random access memory' :
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer=input('What is the full form of CPU? ')
if answer.lower() == 'central processing unit' :
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer=input('What is the full form of PSU? ')
if answer.lower() == 'power supply' :
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer=input('What is the full form of API? ')
if answer.lower() == 'application program interface' :
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
    
print('You got ' + str(score) + 'questions correct!')
print('You got ' + str((score/4)*100) + '%.')
