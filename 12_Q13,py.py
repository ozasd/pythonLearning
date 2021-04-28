# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 14:32:03 2021

@author: user
"""
ipt=input("輸入一字元為:")

ipt=list(ipt)
alist=[]
blist=[]
if len(ipt)/2 !=0:
    ipt.remove(ipt[round(len(ipt)/2)])


for i in range(round(len(ipt)/2)):
    alist.append(ipt[i])
    blist.append(ipt[-i-1])
    
if alist==blist:
    print("YES")
else:
    print("NO")










