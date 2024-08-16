def longestWordLength(string):
    length=0
    for word in string.split():
        if (len(word)>length):
            length=len(word)
    return length
string="I am an intern at geeksforgeeks"
print(longestWordLength(string))
