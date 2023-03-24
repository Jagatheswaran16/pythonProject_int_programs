#input= The sky is blue
#Output= blue is sky The

s="The sky is blue"
print(s)
k=s.split(" ")
l=[]
for i in k[::-1]:
    l.append(i)

l=' '.join(l)
print(l)
