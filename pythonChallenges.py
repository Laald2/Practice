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