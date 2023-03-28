l=[1,2,3,4,5,2,3,1]
print("orginal list", l)
k=[]
a=[]
for i in l:
    if i not in k:
        k.append(i)

    else:
        a.append(i)
print("repeated charcters", a)

print("Ignored repated characters", k)