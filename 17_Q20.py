# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 01:47:08 2021

@author: user
"""


import pandas as pd
number=input("輸入一個學號:")
adict={"學號":["123","456","789","321","654"],
       "姓名":["Tom","Cat","Nana","lim","Won"],
       "系別":["DTGD","CSIE","ASIE","DBA","FDD"]}
table=pd.DataFrame(adict,columns=["學號","姓名","系別"])

for j,k in enumerate(table["學號"]):
    if number==k:
        print("學生資料為:")
        print(table.iloc[j])
    