# String functions are a group of functions that modify strings
# .Lower()


x = "Lord of the Rings"
x = x.lower()
print(x)

question1 = input(str("Who is the goat of stick hockey? \n>"))
question_entered1 = "Benson"
question2 = input(str("Is Mordecai as freaking simp yes or no? \n>."))
question_entered2 = "Yes"


score = 0
if question1 == question_entered1:
    score = score + 1 

if question2 == question_entered2:
    score = score + 1 

print(score)
