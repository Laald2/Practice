'''
https://edabit.com/challenge/RB6iWFrCd6rXWH3vi
'''

def longest_substring(string):
    '''
    Given a string of digits, return the longest substring with 
    alternating odd/even or even/odd digits. If two or more substrings 
    have the same length, return the substring that occurs first.

    Examples
    longest_substring("225424272163254474441338664823") ➞ "272163254"
    # substrings = 254, 272163254, 474, 41, 38, 23

    longest_substring("594127169973391692147228678476") ➞ "16921472"
    # substrings = 94127, 169, 16921472, 678, 476

    longest_substring("721449827599186159274227324466") ➞ "7214"
    # substrings = 7214, 498, 27, 18, 61, 9274, 27, 32
    # 7214 and 9274 have same length, but 7214 occurs first.
    '''
    result = []
    temp_result = []
    prev_check = "even"
    first = True
    for char in string:
        char = int(char)
        if first:
            if get_odd_even(char) == "even":
                prev_check = "even"
            else:
                prev_check = "odd"
            result.append(char)
            first = False
        else:
            if get_odd_even(char) == prev_check:
                if len(result) > len(temp_result):
                    print("SIZE")
                    print(len(result))
                    print(len(temp_result))
                    print("END SIZE")
                    temp_result = result
                print(result)
                result = []
                result.append(char)
                prev_check = get_odd_even(char)
            elif get_odd_even(char) != prev_check:
                result.append(char)
            prev_check = get_odd_even(char)
    if len(temp_result) >= len(result):
        result = temp_result
    final_result = ''
    for char in result:
        char = str(char)
        final_result += char
    print(final_result)
    return final_result

def get_odd_even(num):
    '''
    returns if num is odd or even
    '''
    if num%2 == 0:
        return "even"
    return "odd"


if __name__ == '__main__':
    longest_substring("643349187319779695864213682274")
