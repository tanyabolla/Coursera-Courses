'''
5.1 Exercise 1: Write a program which repeatedly reads numbers until the user enters "done".
Once "done" is entered, print out the total, count, and average of the numbers.
If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.
'''

aSum = 0
count = 0

while True:
    num_input = input("Enter a number: ")
    if num_input == 'done':
        break

    try:
        num = float(num_input)
    except:
        print("Invalid Input")
        continue

    aSum = aSum + num
    count = count + 1

print(aSum, count, aSum/count)
