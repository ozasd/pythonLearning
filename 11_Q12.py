# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 01:09:48 2021

@author: user
"""

in_line=input("輸入一整數序列為:")
#in_line="23 34 34 5 5 34 34"
in_line2=[]
in_line=in_line.split(' ')
for i in in_line:
    in_line2.append(int(i))
    
time_list=[]
alist=[]

in_line2.sort()
for i in in_line2:
    if i not in alist:
        alist.append(i)
        time_list.append(in_line2.count(i))
p=1
for n,i in enumerate(time_list):   
    if len(in_line)/2 < i:
        print("過半元素為:",alist[n])
        p=2
if p==1:
    print("過半元素為:NO")

