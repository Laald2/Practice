'''
This script is just some random challenges at the link below
'''
#https://pythonprinciples.com/challenges/

def capital_indexes(string):
    '''
    Capital indexes
    Write a function named capital_indexes. The function takes a single parameter,
    which is a string. Your function should return a list of all the indexes in
    the string that have capital letters.
    For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].
    '''
    indexes = []
    index = 0
    for char in string:
        if char.isupper():
            indexes.append(index)
        index += 1
    if indexes:
        return indexes
    return 'empty indexes'

def mid(string):
    '''
    Middle letter
    Write a function named mid that takes a string as its parameter.
    Your function should extract and return the middle letter.
    If there is no middle letter, your function should return the empty string.
    For example, mid("abc") should return "b" and mid("aaaa") should return "".
    '''
    size_str = len(string)
    mid_index = size_str/2
    if mid_index.is_integer():
        print("ERROR no middile letter")
    if not mid_index.is_integer():
        return string[int(mid_index)]
    return "no middile letter"



def online_count(online_status):
    '''
    Online status
    The aim of this challenge is, given a dictionary of people's online status,
     to count the number of people who are online.

    For example, consider the following dictionary:

    statuses = {
        "Alice": "online",
        "Bob": "offline",
        "Eve": "online",
    }
     In this case, the number of people online is 2.

    Write a function named online_count that takes one parameter.
    The parameter is a dictionary that maps from strings of names
    to the string "online" or "offline", as seen above.

    Your function should return the number of people who are online.
    '''
    online_num = 0
    for key in online_status:
        if online_status[key] == 'online':
            online_num += 1
    return online_num

if __name__ == '__main__':
    mid("123")
