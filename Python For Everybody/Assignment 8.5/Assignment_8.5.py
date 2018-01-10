'''
8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message).
Then print out a count at the end.
Hint: make sure not to include the lines that start with 'From:'.

You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
'''

#Open a file
fhand = open("mbox-short.txt")

#Initialize count
count = 0

#Go through the file line by line
for line in fhand:
    #Strip the newline character from the end of the lines
    rsline = line.rstrip()
    #Split the line by spaces
    sline = rsline.split()
    #If the line does not contain a from in the line, continue
    if 'From' not in sline:
        continue
    #If the line does contains a from, print the second word of that line.
    print(sline[1])
    #Increase the count
    count += 1

#Print the counter along with a statement
print("There were", count, "lines in the file with From as the first word")
