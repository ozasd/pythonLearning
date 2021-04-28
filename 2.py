

do=int(input("輸入一個度數(正整數)>>>"))

tol1=0
tol2=0
dolist=[120,330,500,700,99999]#度數清單
alist=[3.02,4.39,4.97,5.63]
blist=[2.68,3.61,4.01,4.50]    


if do <= 120:
    tol1,tol2=do*2.1,do*2.1
    print("Summer months:",round(tol1,2),'\nNon-Summer months:',round(tol2,2))
else:
    tol1,tol2=120*2.1,120*2.1
    
    for j,k in enumerate(dolist):
        
        
        
        if do > dolist[j] and do <= dolist[j+1]:
            
            tol1+=(do-dolist[j])*alist[j]
            tol2+=(do-dolist[j])*blist[j]
            
            print("Summer months:",round(tol1,2),'\nNon-Summer months:',round(tol2,2))
            break
        else:
            
            tol1+=(dolist[j+1]-dolist[j])*alist[j]
            tol2+=(dolist[j+1]-dolist[j])*blist[j]
            
        


