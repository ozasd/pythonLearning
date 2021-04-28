# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 22:02:07 2021

@author: user
"""


number=input()
n=[]
for i in number:
    n.append((int(i)+7)%10)
    
print("輸出加密後的數字為:",n[2],n[3],n[0],n[1])