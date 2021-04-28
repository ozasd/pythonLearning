# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 13:23:10 2021

@author: user
"""

m=1000
m=int(input("請輸入階乘值 M:"))
total=1
n=0


while m > total:
    total=1
    n+=1
    for i in range(1,n+1):
        total*=i
else:
    print(f"超過M為{m}的最小階乘 N值為:{n}")
    
    