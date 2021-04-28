# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 22:20:25 2021

@author: user
"""
chr1=[]
for i in range(2):
    chr1.append(input(f"請輸入S{i+1}:"))

word1=list(chr1[0])
word2=list(chr1[1])
word3=[]

for _ in range(len(word2)-len(word1)+1):
    combine=''
    for i in range(len(word1)):
        combine+=word2[i]
        word3.append(combine)
    word2.pop(0)
    
if chr1[0] in word3:
    print("YES")
else:
    print("NO")
    