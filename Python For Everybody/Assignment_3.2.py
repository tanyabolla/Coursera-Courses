'''
3.2 Rewrite the  pay program from Assignment 3.1 using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program.
The following shows two executions of the program:
'''

hours = input("Enter hours: ")
rph = input("Enter hourly rate: ")

'''
try:
    fhrs = float(hours)
except:
    print("Error. Enter a numeric input.")

try:
    frph = float(rph)
except:
    print("Error. Enter a numeric input.")
'''
#Do this, because both data has to be numerical for the program to work
try:
    fhrs = float(hours)
    frph = float(rph)
except:
    print("Error. Enter a numeric input.")
    quit()

if fhrs > 40.0:
    pay = (40 * frph)
    overhrs = fhrs - 40.0
    overpay = overhrs * frph * 1.5
    print(pay + overpay)
else:
    print(fhrs * frph)
