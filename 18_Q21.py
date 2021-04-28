import pandas as pd 
damo={"帳號":[123,456,789,336,775,566],
      "密碼":[456,789,888,558,666,221],
      "餘額":[9000,5000,6000,10000,12000,7000]}
demo=pd.DataFrame(damo)

n=int(input("輸入查詢組N為:"))

for _ in range(n):
    Error=False
    ipt=input(">>>")
    ipt=ipt.split(' ')

    for j,k in enumerate(demo["帳號"]):
        if k== int(ipt[0]):
            if demo["密碼"][j] == int(ipt[1]):
                print(demo["餘額"][j])
                Error=True
        
    if Error==False:
        print("Error")