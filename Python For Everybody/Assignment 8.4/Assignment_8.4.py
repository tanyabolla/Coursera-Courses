'''
8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method.
The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list.
When the program completes, sort and print the resulting words in alphabetical order.
You can download the sample data at http://www.py4e.com/code3/romeo.txt
'''
#Opens the file
fhand = open("romeo.txt")

#Empty list
words = []

#Splits the file
for line in fhand:
    #Strip the \n at the end of the line
    rsline = line.rstrip()
    #Split the line using the spaces
    sline = rsline.split()
    #For each word in the line, see if the word already exists in a list
    for word in sline:
        if word not in words:
            words.append(word)

#Sort the words in the list alphabetically
words.sort()
#Print all the words in the list
print(words)
