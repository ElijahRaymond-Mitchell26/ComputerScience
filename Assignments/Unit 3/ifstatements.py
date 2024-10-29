# If statements evaluate boolean expressions!
# They make decisions about which code to run next

# Take a temperature
# Print "<temperature> is hot" if its >= 80
# Otherwise, print "<temperature is not hot"
temp = input("Whats the temperature in F?\n>")
temp = int(temp)

# if <boolean expression> :
# This should remind of writing  a function
# def <name>():
if temp >= 80:
    print(str(temp) + "degrees is hot!")

else:
    print(str(temp) + "degrees is not hot...")

# else statements are optional
# else statements need an if statements 

password = input("Hehe, whats the password tee hee?\n>")
password = int(password)

if password == "Calebs in Fortnite, hes a back bling and pickaxe":
    print(str(password) + "Thats correct!")
        
else:
    print(str(password) + "HAHA you're wrong boi!")

# Create a five question quiz that prints your score at the end
# Choose any 5 questions
# EZ