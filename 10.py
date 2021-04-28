# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 00:24:48 2021

@author: user
"""

import numpy as np
aList=[]
ipt=input("請輸入N及M為:")
ipt=ipt.split(" ")

for b in range(int(ipt[0])):
    r_line=input(f"輸入矩陣第{b+1}列數值為:")
    aList+=list(r_line.split(" "))
    

table=np.array(aList)
table=table.reshape(int(ipt[0]),int(ipt[1]))
table=table.T
for n,i in enumerate(table):
    print(f"輸出矩陣第{n+1}列為:",end="")
    for r in i:
        print(r,end=' ')
    print("\n")
        

