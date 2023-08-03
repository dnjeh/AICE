import pandas as pd
import numpy as np

#비슷비슷한 데이터프레임들을 합치는 데 적합한건.. concat!

df1 = pd.DataFrame({"key1" : [0,1,2,3,4], "value1" : ['a', 'b', 'c', 'd', 'e']}, index=[0,1,2,3,4])
df2 = pd.DataFrame({"key1" : [3,4,5,6,7], "value1" : ['c', 'd', 'e', 'f', 'g']}, index=[3,4,5,6,7])
print(df1)
print(df2)

print(pd.concat([df1, df2], ignore_index=False))
print(pd.concat([df1, df2], axis=1))

df3 = pd.DataFrame({'a':['a0','a1','a2','a3'], 'b':['b0','b1','b2','b3'], 'c':['c0','c1','c2','c3']}, index=[0,1,2,3])
df4 = pd.DataFrame({'a':['a2','a3','a4','a5'], 'b':['b2','b3','b4','b5'], 'c':['c2','c3','c4','c5'], 'd':['d0','d1','d2','d3']}, index=[0,1,2,3])
print(df3)
print(df4)

print(pd.concat([df3, df4], join="outer"))
print(pd.concat([df3, df4], join="inner"))

df5=pd.DataFrame({'A':["A0", "A1", "A2"], 'B':["B0", "B1", "B2"], 'C':["C0", "C1", "C2"], 'D':["D0", "D1", "D2"]},index=["I0", "I1", "I2"])
df6=pd.DataFrame({'A':["AA2", "A3", "A4"], 'B':["BB2", "B3", "B4"], 'C':["CC2", "C3", "C4"], 'D':["DD2", "D3", "D4"]},index=["I2", "I3", "I4"])
print(df5)
print(df6)

print(pd.concat([df5, df6], verify_integrity=False))
#print(pd.concat([df5, df6], verify_integrity=True)) 중복된 인덱스이므로 에러!

#일반적인 데이타-프레임들을 합친다면, merge와 join!

customer = pd.DataFrame({"cust_id" : np.arange(6),
                         "name" : ["철수", "영희", "길동", "영수", "수민", "동건"],
                         "나이" : [40,20,21,30,31,18]})
orders = pd.DataFrame({"cust_id" : [1,1,2,2,2,3,3,1,4,9],
                         "item" : ["치약", "칫솔","이어폰","헤드셋","수건","생수","수건","치약","생수","케이스"],   
                         "quantity" : [1,2,1,1,3,2,2,3,2,1]})
print(customer)
print(orders)

print(pd.merge(customer, orders, on="cust_id"))

print(pd.merge(customer, orders, on="cust_id", how="inner")) #기본값인듯
print(pd.merge(customer, orders, on="cust_id", how="left")) #왼쪽 기준
print(pd.merge(customer, orders, on="cust_id", how="right")) #오른 쪽 기준
print(pd.merge(customer, orders, on="cust_id", how="outer")) #합집합!

#인덱스야~ 놀자~! 

cust1=customer.set_index("cust_id")
order1=orders.set_index("cust_id")
print(cust1)
print(order1)

print(pd.merge(cust1, order1, left_index=True, right_index=True))

#연습 1번, 가장 많이 팔린 아이템!

print(pd.merge(customer, orders, on="cust_id", how="right").groupby("item").sum())
print(pd.merge(customer, orders, on="cust_id", how="right").groupby("item").sum().sort_values(by="quantity", ascending=False))

#연습 2번, 영희가 가장 많이 구매한 아이템!

print(pd.merge(customer, orders, on="cust_id", how="inner").groupby(["name", "item"]).sum())
print(pd.merge(customer, orders, on="cust_id", how="inner").groupby(["name", "item"]).sum().loc["영희"])

#겸사겸사 알아가는 join
print(cust1.join(order1, how="inner")) #인덱스로 합쳐요!