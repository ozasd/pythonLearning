prime=input("請輸入正整數>>>")

primelist=[]
alist=[]
blist=[]
for a in range(len(prime)):
    for i in range(len(prime)+1):
        primelist.append(prime[a:i])


while "" in primelist:
    primelist.remove("")
for i in primelist:
    alist.append(int(i))
alist.sort()
alist.reverse()
for f in alist:
    for g in range(2,f):
        if f%g == 0:
            blist.append(f)
p=0
for c in alist:
    if c not in blist:
        print(c)
        p+=1
        break
if p==0:
    print("No prime found")