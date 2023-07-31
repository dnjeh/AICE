x="Rome is not built in a day!"

#indexing
print(x[0])

print(x[-1]) #%연산자를 생각해바!.!

print(x[-6])

print(x[12])

#slicing

print(x[0:4]) #0번부터 4번 직전까지 출력!

print(x[12:]) #비워두면 마지막까지,

print(x[:-7]) #비워두면 처음부터!, -x 사용 가능!

print(x[:]) #둘다 비우면 온전해지는!

############################Part 2##############################

#list

a=[1,2,3] #기본적으로 [] 을 써서 만든다
print(a)

b=list(range(1,10,2)) #range() 쓰거나 리스트 컴프리헨션 ㄲ
print(b)

##func

a=["red", "green", "blue"]
a.append("yellow") #리스트 뒤에 붙이거나..
print(a)

a.insert(1, "black") #위치를 정해서 삽입할 수도 있고
print(a)

b=["purple", "white"]
a.extend(b) #이어붙이기까지!
print(a)

c=a+b ##이렇게 할 수도 있다.
print(c)

d=[i for i in range(10, 101, 10)] #이거시 리스트컴프리헨션!
d.remove(90) #값을 없앤다.
print(d)

list1=['a', "bb", 'c', 'd', "aaa", 'b', "cc", 'd', "aaa", ]
print(list1.count("aaa")) #일치하는 요소의 갯수를 세서 반환!

list2=[1, -7, 5, 8, 3, 9, 11, 13]
list2.sort() #우리 파이썬은 오름차순 정렬도 기본 내장이고요
print(list2) 

list2.sort(reverse=True) #내림차순도 기본이애오
print(list2)

d=[i for i in range(10, 101, 10)]
d.pop(0) #특정 위치에 있는 값을 지우고 호출하거나, 인자가 없으면 그냥 스택처럼 작동함.
print(d)

#Tuple

t1 = ("banana", "apple", "kiwi") #괄호 이용함. 이게 몬,..
print(t1)

t2 = "banana", "apple", "kiwi" #그냥 나열해도 튜플이다. ..이개몬!@@!!@
print(t2)

#t2[0] = "watermelon" # 번경 불가능한 리스트가 곧 튜플이다. 그렇기 때문에 관련 람수도 못씀.

#Dictionary

members = {"name":"인자명", "age":30, "email":"jiyoung@korea.com"} #딕셔너 리(23) 는 키와 밸브 값으로 이루어짐, 키값엔 튜플만 사용 가능! 

print(members.keys()) #이건 키값 호출
print(members.values()) #이건 밸류 호출
print(members.items()) #아이템, 그러니깐 한 쌍씩 허출해주고요
print(members.get("name")) #키값에 대응하는 밸류도 가져와줌

print("name" in members) #딕셔너 리(12) 에 있는지 없는지 판별! 이건 True 고
print("birth" in members) #이건 False임. false 아님.

members.clear() #마지막으로 free() 해준다.
print(members) 
