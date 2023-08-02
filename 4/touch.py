import pandas as pd
import numpy as np

cust = pd.read_csv("./4/sc_cust_info_txn_v1.5.csv", encoding="cp949")
print(cust)

#묶자! (group by)

gender_group = cust.groupby("sex_type")
print(gender_group)
print(gender_group.groups)
print(gender_group.count())
#print(gender_group.mean()) 평균! 인데.. 실행이 안댐.
print(gender_group.max())
#gender_group.mean()[["r3m_avg_bill_amt"]]
#cust.groupby("sex_type").mean()[["r3m_avg_bill_amt"]] 실행은 안 대지만.. 원형은 댐.

#cust.groupby(["cust_class", "sex_type"]).mean()[["r3m_avg_bill_amt"]] #복수의 column도 대고, 이건 멀티인덱스로 들어감!

#multi_group=cust.groupby(["cust_class", "sex_type"])
#multi_group.mean()[["r3m_avg_bill_amt"]]

#cust.groupby(["cust_class", "sex_type"]).mean().loc[[("D","M")]] #똑같이 작동함!.!

print(cust.head())

print(cust.set_index(["cust_class", "sex_type"])) #set_index 자체가 groupby 효과를 내기도 함!
print(cust.set_index(["cust_class", "sex_type"]).reset_index())  #원.상.복.구.

print(cust.set_index(["cust_class", "sex_type"]).groupby(level=[0]).sum()) #인덱스 기준으로 groupby! [0]은 cust_class를 의미하는..
print(cust.set_index(["cust_class", "sex_type"]).groupby(level=[0,1]).sum()) #당연히 이것도 여러개 가능!
print(cust.set_index(["cust_class", "sex_type"]).groupby(level=[0,1]).aggregate([np.sum, np.max])) #여러가지 값들을 묶어서 볼 숟조 잇음!.!

#행열 열행 신나는 노래~ (pibot)

data = pd.DataFrame({ #오랜 만이 지
    "cust_id" : ["cust_1", "cust_1", "cust_1", "cust_2", "cust_2", "cust_2", "cust_3", "cust_3", "cust_3"],
    "prod_cd" : ["p1", "p2", "p3", "p1", "p2", "p3", "p1", "p2", "p3"],
    "grade" : ['A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B'],
    "pch_amt" : [30, 10, 0, 40, 15, 30, 0, 0 ,10]
})
print(data)

print(data.pivot(index="cust_id", columns="prod_cd", values="pch_amt"))
#print(data.pivot("cust_id", "prod_cd", "pch_amt"))  #같은 역할이여야 하는데.. 달?름
print(data.pivot_table(index="cust_id", columns="prod_cd", values="pch_amt")) #얜 aggfunc 도 쓸 수 잇 다!

print(data.pivot_table(index=["cust_id","grade"], columns="prod_cd", values="pch_amt")) #이거 pivot 은 안댐! 멀티 인덱스도 댐!
print(data.pivot_table(index="cust_id", columns=["grade", "prod_cd"], values="pch_amt")) #이거 pivot 은 안댐2! 심지어 컬럼들 여러개 잇어도 댐!!
print(data.pivot_table(index="grade", columns="prod_cd", values="pch_amt")) #이거 pivot 은 안댐3! index에 중복있어도 댐!!!

print(data.pivot_table(index="grade", columns="prod_cd", values="pch_amt", aggfunc=np.sum)) #기본적으로 평균을 주지만, 수정 가능 pivot은 안댐!!!!
#print(pd.pivot_table(data, index="grade", columns="prod_cd", values="pch_amt", aggfunc=np.sum)) #심지어 첫 인자로 data를 줄 수도!

#님 어디서 만이 보지 안았어요? 상역, 하역! (stack, unstack)

df = pd.DataFrame({
    "지역" : ["서울", "서울", "서울", "경기", "경기", "부산", "서울", "서울", "부산", "경기", "경기", "경기"],
    "요일" : ["월요일", "화요일", "수요일", "월요일", "화요일", "월요일", "목요일", "금요일", "화요일", "수요일", "목요일", "금요일"], 
    "강수량" : [100, 80, 1000, 200, 200, 100, 50, 100, 200, 100, 50, 100],
    "강수확률" : [80, 70, 90, 10, 20, 30, 50, 90, 20, 80, 50, 10]
})

print(df)

new_df=df.set_index(["지역", "요일"])
print(new_df)

print(new_df.unstack(0)) 
print(new_df.unstack(1))