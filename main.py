firstName = 'Srikar'
lastName = 'Kotha'

fullName = firstName + " " + lastName
print('My name is: ' + fullName + ', not done yet...')

score1 = 34  # int(input('score1: '))
score2 = 56  # int(input('score2: '))
finalScore = score2 - score1
print('Result: ', str(score2 - score1), 'end of program...')

print("My name is: %s, my score is %i" % (fullName, finalScore))
print('My name: {}, my score: {}' .format(fullName, finalScore))
#or
print('My name: {first}, my score: {second}' .format(first=fullName, second=finalScore))
print(f'My name: {fullName}, my score: {finalScore}')


# 1. plain format, passing multiple values
# 2. string concatinate: joing two string
# 3. using % format
# 4. using format()
# 5. using f-string
