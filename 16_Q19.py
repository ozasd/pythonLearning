# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 01:34:31 2021

@author: user
"""

def counting(x):
    x=x.split(" ")
    return 250*int(x[0])+175*int(x[1])
    
n=int(input("組數為:"))

for i in range(n):
    ipt=input(f"第{i+1}組:")
    print(f"第{i+1}組應收費用:",counting(ipt))