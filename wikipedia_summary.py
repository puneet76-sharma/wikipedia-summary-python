# pip install wikipedia

import wikipedia as w

# finding result for the search

# sentences = 2 refers to number of line

text= input("Search Wikipedia: ")
result= w.summary(text)
print(result)

input()