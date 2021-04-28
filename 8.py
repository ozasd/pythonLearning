# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 19:16:54 2021

@author: user
"""



a=input("輸入第一行正整數為:")
#ipt="1 4 6 2 3 5 8 7"
ipt=input("第二行數列中的數字為:\n ex:1 4 6 2 3 5 8 7\n:")
time=[]

alist=[]
blist=[]
number=list(ipt)
while " " in number:
    number.remove(" ")
number.sort()

for n,a in enumerate(number):
    if a in number:
        time.append(number.count(a))
        
for n,i in enumerate(time):
    if i > 1 and number[n] not in alist:
       alist.append(number[n])
       blist.append(i)
       
       
if len(blist)==0:
    print("每個數字剛好只出現一次")
else:
    print("最大出現次數的數字為:",alist[-1])
    print("出現次數為:",blist[-1])

