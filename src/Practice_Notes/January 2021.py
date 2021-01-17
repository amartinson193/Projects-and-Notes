
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

# def solution(number):
#     total = 0
#     for i in range(number):
#         if (i % 3 == 0 or i % 5 == 0) and i >= 0:
#             total += i
#     return total
# print(solution(100))

# 1/13/21 --------------------------------------------------------------------

# Codewars challenge - Find the odd int - 6kyu --------------------------------

# import pandas as pd

# def find_it(seq):
#     x = (pd.Series(seq).value_counts() % 2 > 0)
#     return int(x[x].index.values)

# print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))

# Codewars challenge - Find the odd int - 6kyu --------------------------------

# def song_decoder(song):
#     return song.replace('WUB',' ').split(' ')

# print(song_decoder('AAWUBWUBBWUBC'))

# 1/14/21

# Datacamp - Statistical Thinking Part 1 --------------------------------

# import numpy as np
# import matplotlib.pyplot as plt

# plt.plot(np.random.random(10))
# plt.show()

# Codewars - Persistent Bugger - 6kyu --------------------------------

# import numpy as np

# import numpy as np

# def persistence(n):
#     x = np.prod([int(i) for i in str(n)])
#     count = 0
#     while x > 9:
#         x = np.prod([int(i) for i in str(x)])
#         count += 1
#     return count + 1 if n > 9 else 0

# Random --------------------------------
# import functools

# print(functools.reduce(lambda x,y: x+y,[1,2,3]))

# print({'hi':1,'bye': 2}.get(['hi','bye'],'Not Here!'))
# s = [1,2,3]
# print(s.index(2))

# import operator 
# import functools

# s = ['hi',1]
# print(itemgetter('hi')(s))

# s = [('hi',10),('bye',5)]
# for i in dict(s).items():
#     print(i[0])
# print(s.sort(key=itemgetter(1)))

# x = functools.reduce(operator.add,[1,2,3],5))

# Codewars Title Case -------------------------------

# def title_case(title, minor_words=''):
#     new_title = title.title()
#     for i in new_title.split():
#         if i.lower() in minor_words.lower().split() and new_title.split().index(i) > 0:
#             new_title = new_title.replace(i,i.lower())
#     return new_title

# print(title_case('THE WIND IN THE WILLOWS', 'The In'))

# 1/16/21

import numpy as np

# print(np.corrcoef([1,2,3,4,10],[1,2,3,4,5]))
# print([1,2]*2)

# arr = []
# arr.append([1,2,3])
# arr.append([4,5,6])
# np_arr = np.array(arr)
# print(np_arr)

# print(np.append([1, 2, 3], [[4, 5, 6], [7, 8, 9]]))

import numpy as np
from icecream import ic

arr = [1,2,3]
for i in range(5):
    arr = np.append(arr,[0,i])
    ic()
print(arr)

# ls = []
# for i in range(5):
#     ls.append(0)
# print(ls) 

# from icecream import ic
# ic('hello world')

