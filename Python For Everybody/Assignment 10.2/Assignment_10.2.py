'''
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
'''
#Open the file mbox-short
fhand = open("mbox-short.txt")
#Create an empty dictionary
hours = dict()

#For every line in the file,
for line in fhand:
    #Split the file using spaces
    sline = line.split()
    #If 'From' not in the line, continue
    if 'From' not in sline:
        continue
    #Take the 6th place in the line, and split it by a colon
    splitline = sline[5].split(':')
    #Put the hour in the dictionary
    #If it already exists, add one to it
    hours[splitline[0]] = hours.get(splitline[0], 0) + 1

#Create an empty list
sort = list()
#Print how many each hours appears
for k, v in hours.items():
    sort.append((k, v))

#Sort the list
slist = sorted(sort)

#Print the tuples in the list
for key, val in slist:
    print(key, val)
