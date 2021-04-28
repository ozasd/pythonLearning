# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 23:34:19 2021

@author: user
"""
adict={"A":1,"J":11,"Q":12,"K":13}
ipt=input(">>>")
rmList=[]
total=0
ipt=ipt.split(" ")
for i in ipt:
    if i in adict:
        ipt.append(adict[i])
        rmList.append(i)
for i in rmList:
    if i in ipt:
        ipt.remove(i)
for i in ipt:
    total+=int(i)
    
print(total)


           
        
