# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 13:43:20 2021

@author: user
"""


ipt=input("輸入值為:")
min_=""
max_=""
alist=list(ipt)
while "," in alist:
    alist.remove(",")
else:
    alist.sort()
    for i in alist:
        min_+=i
    alist.reverse()
    for i in alist:
        max_+=i
    print("最大值數列與最小值數列差為:",int(max_)-int(min_))