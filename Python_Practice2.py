#While loop statement: 
x = 0
while x <=5: 
    print(x)
    x = x + 1

#for loop statement: 
for x in range(5):
    print(x)



#test if Else 
temperature = int(input("What is the temperature outside? "))
if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.")
print("\n")
#Print Nested Ifs using grades
score = int(input("What is your test score?"))
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')


   # Import the datetime class from the datetime module.
import datetime
# Use the now() attribute on the datetime class to get the present time.
now = datetime.datetime.now()
# Print the present time.
print("The time right now is ", now) 