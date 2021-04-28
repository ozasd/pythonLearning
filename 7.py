# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 18:01:51 2021

@author: user
"""
total=0
ipt=input("請輸入月租費形式及通話時間為:\n ex:386,36000\n:")
#ipt="386,36000"
ipt=ipt.split(",")

feelist=[186,386,586,986]
ratelist=[0.09,0.08,0.07,0.06]
discount=[0.9,0.8,0.7,0.6]
doubleDis=[0.8,0.7,0.6,0.5]


for n,i in enumerate(feelist):   
    if int(ipt[0]) == i:
        total=int(ipt[1])*ratelist[n]
        if total <= feelist[n]:
            total=feelist[n]
        elif feelist[n]<total <=(feelist[n]*2):
            total=total*discount[n]
        elif total>(feelist[n]*2):
            total=total*doubleDis[n]
    else:
        print("輸入錯誤")
        break
            
print("通話費為:",round(total))
            
            