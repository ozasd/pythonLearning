# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 13:02:59 2021

@author: user
"""

#x,y=0,2
x=int(input("X軸座標:"))
y=int(input("Y軸座標:"))
qd=None
if x==0 and y==0:
    print("該點位於原點")
    
elif x==0 and y>0:
    qd="上半平面y軸上"
elif x==0 and y<0:
    qd="下半平面y軸上"
elif x>0 and y==0:
    qd="右半平面x軸上"
elif x<0 and y==0:
    qd="左半平面x軸上"
elif x>0 and y>0:
    qd="第一象限"
elif x<0 and y>0:
    qd="第二象限"
elif x<0 and y<0:
    qd="第三象限"
elif x>0 and y<0:
    qd="第四象限"
if qd!= None:
    
    print(f"該點位於{qd}，離原點距離為根號{x**2+y**2}")
