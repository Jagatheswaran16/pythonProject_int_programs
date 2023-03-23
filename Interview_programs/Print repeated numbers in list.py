l=[1,2,3,4,5,2,3,1]
k=[]
for i in l:
    if i not in k:
        k.append(i)

    else:
        print("repeated charcters", i)

print("Ignored repated characters", k)