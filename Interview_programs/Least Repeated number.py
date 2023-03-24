import collections
from collections import Counter

s=input("enter a string")


result= Counter(s)

result=min(result, key=result.get)
print(result)