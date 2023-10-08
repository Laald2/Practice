#https://pythonprinciples.com/challenges/

'''
Capital indexes
Write a function named capital_indexes. The function takes a single parameter, 
which is a string. Your function should return a list of all the indexes in the string that have capital letters.
For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].
'''

def capital_indexes(string):
    indexes = []
    index = 0
    for char in string:
        if (char.isupper()):
            indexes.append(index)
        index += 1
    return indexes

'''
Middle letter
Write a function named mid that takes a string as its parameter.
 Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.
For example, mid("abc") should return "b" and mid("aaaa") should return "".
'''

def mid(string):
    size_str = len(string)
    midIndex = size_str/2
    if midIndex.is_integer():
        return ""
    else:
        return string[int(midIndex)]

 '''
 Online status
The aim of this challenge is, given a dictionary of people's online status, to count the number of people who are online.

For example, consider the following dictionary:

statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}
In this case, the number of people online is 2.

Write a function named online_count that takes one parameter. 
The parameter is a dictionary that maps from strings of names to the string "online" or "offline", as seen above.

Your function should return the number of people who are online.
 '''

def online_count(dict):
    onlineNum = 0
    for key in dict:
        if dict[key] is 'online':
            onlineNum += 1
    return onlineNum