f=open("text_file.txt")
f=f.read()
f1=f.split(" ")
k={}
print(f1)
for i in f1:
    if i in k:
        k[i] = k[i] + 1
    else:
        k[i] = 1
print(k)
r = max(k, key=k.get)
print(r)