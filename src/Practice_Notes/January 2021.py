
# 1/12/2021

# Codewars challenge ---------------------------------

# def validBraces(string):
#     sets = {'{':'}','[':']','(':')'
#            , '}':None,']':None,')':None}
#     if type(string) == str:
#         string = [char for char in string]
#     count = 0
#     while count + 1 < len(string):
#         if string[count + 1] == sets[string[count]]:
#             del string[count: count + 2]
#             validBraces(string)
#         count += 1
#     return True if len(string) == 0 else False       

# validBraces('{}[{}{}[[[]]]]]')

# Codewars challenge ---------------------------------

# import string 

# def is_pangram(s):
#     return all([x in s.lower() for x in string.ascii_lowercase])
# s = string.ascii_lowercase + 'BSDASDASD'
# print(is_pangram(s))

# Codewars challenge - Multiples of 3 or 5 - 6 kyu --------------------------------

def solution(number):
    total = 0
    for i in range(number):
        if (i % 3 == 0 or i % 5 == 0) and i >= 0:
            total += i
    return total
print(solution(100))