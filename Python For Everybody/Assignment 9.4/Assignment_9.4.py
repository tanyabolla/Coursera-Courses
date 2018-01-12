'''
9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages.
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
Check Code
'''

#Open a file
fhand = open("mbox-short.txt")

#Initialize dictionary
words = dict()

#Go through the file line by line
for line in fhand:
    #Strip the newline character from the end of the lines
    rsline = line.rstrip()
    #Split the line by spaces
    sline = rsline.split()
    #If the line contains a from in the line, add the second word to the dictionary
    if 'From' in sline:
        words[sline[1]] = words.get(sline[1], 0) + 1

#Initialize count variables
count = None
email = None

#Loop through the dictionary to find the most common email address
for k, v in words.items():
    if count is None or v > count:
        email = k
        count = v

#Print out the email address that appeared the most and how many times it appeared
print(count, email)
