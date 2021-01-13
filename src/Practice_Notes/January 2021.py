
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

import string 

def is_pangram(s):
    return all([x in s.lower() for x in string.ascii_lowercase])
s = string.ascii_lowercase + 'BSDASDASD'
print(is_pangram(s))