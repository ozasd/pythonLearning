#ipt="72"
ipt=input("請輸入正整數:")
indexList=[]
rmlist=[]
for a in range(len(ipt)):
    for i in range(len(ipt)+1):
        if ipt[a:i] != "":
            if int(ipt[a:i]) not in indexList:
                indexList.append(int(ipt[a:i]))

indexList.sort()



for i in indexList:
    for a in range(2,i):
        if i%a == 0:
            if  i not in rmlist:
                rmlist.append(i)
for i in rmlist:          
    indexList.remove(i)

if len(indexList) == 0:
    print("子字串最大質數質為:No Prime Found")
else:
    print(f"子字串最大質數質為:{indexList[-1]}") 