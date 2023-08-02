import pandas as pd
import numpy as np
from IPython.display import Image
import matplotlib.pyplot as plt

#데이타-프레이무 란?
a1 = pd.DataFrame({'a' : [1,2,3], 'b' : [4,5,6], 'c' : [7,8,9]})
print(a1) #디렉토리로 만들 수도 있고

a2 = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]], ['a','b','c'])
print(a2) #리스트로도!

cust = pd.read_csv("./4/sc_cust_info_txn_v1.5.csv", encoding="cp949") #파일로 만들기! 가장 마늠
print(cust)
print(cust.head(n=3))
print(cust.head(n=10))
print(cust.shape)
print(cust.columns)
print(cust.info())
print(cust.describe())
print(cust.dtypes)

cust2=pd.read_csv("./4/sc_cust_info_txn_v1.5.csv", index_col="cust_class", usecols=["cust_class", "r3m_avg_bill_amt", "r3m_B_avg_arpu_amt", "r6m_B_avg_arpu_amt"])
print(cust2) #usecols 안엔 반드시 인덱스col 이 필요!.!

#데이터 조회하기!

cust.cust_class = cust["cust_class"]
print(cust.cust_class) #column 선택해서 가져오거나, ([]안에 col쓰기!)

print(cust[["cust_class"]])

print(cust[["cust_class", "age", "r3m_avg_bill_amt"]])

print(cust[7:10]) #이건 row 단위로 잘라옴! 

print(cust.info())

#cp=np.arange(10, 20) 
#print(cp) array 로 반환하는 range!
cust.index = np.arange(10, 40)
print(cust) #index를 일단 바꿔주고,
print(cust.tail())

print(cust.loc[[30]])
print(cust.loc[[30, 35, 39]]) #이건 쓰여진 값!
print(cust.iloc[[20, 25, 29]]) #이건 고정값!

print(cust.loc[[10, 20, 30], ["cust_class", "sex_type", "age", "r3m_avg_bill_amt"]])
print(cust.iloc[[0, 10, 20], [3, 4, 5, 9, 10]]) #오로지 인덱스만!.!.! loc은 에러난다--

extract = cust[(cust["sex_type"]=='M') & (cust["r3m_avg_bill_amt"]>=50000) & (cust["r3m_avg_bill_amt"]<100000)]
print(extract.head()) #조건문에 만족하는 애들만 알아서 대려옴!! 
#혹은,
sex=cust["sex_type"]=='M'
bill=(cust["r3m_avg_bill_amt"]>=50000) & (cust["r3m_avg_bill_amt"]<100000)
print(cust[sex&bill].head())

#데이터 수정-추가하기!
cust["r3m_avg_bill_amt2"] = cust["r3m_avg_bill_amt"] * 2 #곱셈은 각 row에서 2배씩 해서 맨 뒤에ㅡ
print(cust[["r3m_avg_bill_amt", "r3m_avg_bill_amt2"]])

cust["r3m_avg_bill_amt3"] = cust["r3m_avg_bill_amt2"] + cust["r3m_avg_bill_amt"]
print(cust[["r3m_avg_bill_amt", "r3m_avg_bill_amt2", "r3m_avg_bill_amt3"]]) #덧셈은 그냥 더해서.

cust.insert(10, "r3m_avg_bill_amt10", cust["r3m_avg_bill_amt"]*10)
print(cust.head()) #insert 하면 인덱스의 위치에 추가.

#데이터 수정-삭제하기..
cust.drop("r3m_avg_bill_amt10", axis=1) #지우고자 하는 column을 적고, 가로 혹은 세로를 설정한 뒤, 지웠었지만..
print(cust.head()) #원본은 상관 없음. 즉, 지웠던 함수를 어디에 넣어야한다는,,
#지우려고 한다면

cust1=cust.drop("r3m_avg_bill_amt10", axis=1)
print(cust1.head()) #이렇게 다른 곳에 넣거나

cust.drop("r3m_avg_bill_amt10", axis=1, inplace=True)
print(cust) #inplace를 참으로 설정하여, 원본까지 영향을 끼치거나!