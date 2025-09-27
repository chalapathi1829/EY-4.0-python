#print hello world
# print("Hello world")

# # variables
# a=20
# b=30
# #assiging 
# c,d=a,b
# print(a,b,c,d)
# a=b=10
# c=d=a
# print(a,b,c,d)
# #assigning multiple values to multiple variables in one line
# x,y,z=10,20,30
# print("x:",x,"y:",y,"z:",z)

#Data Types printing
# name="Jhon"
# age=23
# phone="9988775566"
# #type
# print(type(name),type(age),type(phone))

#Time calculation
# hours=24
# oneweek=7
# onemonth=30
# oneyear=365
# print("Hours per one Day:",hours,"hours")
# print("Hours per one week:",oneweek*hours,"hours")
# print("Hours per one month:",onemonth*hours,"hours")
# print("Hours per one Year:",oneyear*hours,"hours")

#calculating minutes for a given number
# num=int(input("Enter a number:"))
# print("Total number of minutes for",num,"hours is:",num*60)


#calculate days based on age
# age=int(input("Enter age:"))
# print("age:",age," total days:",age*365)

#data structures
# tuple=(22,'jhon',23)
# print(type(tuple))
# set={11}
# print(type(set))
# lists=[1,2,3,4]
# print(type(lists))
# dict={"name":"jhon","age":22}
# print(type(dict))

# print(lists[1])
# print(dict["name"])
# print(list(set)[0])
# print(tuple[2])

#if condition
# a=int(input("Enter your attendance:"))
# if a>=70:
#     print("your attendance is",a,".","your are Eligible")
# else:
#     print("your attendance is",a,".","your are not Eligible")

#if condition in oneline
# a=4
# print("even") if a%2==0 else print("odd")

# validating password
# username="admin"
# password="admin@123"

# a=input("enter username:")
# b=input("Enter password:")
# if (a==username and b==password):
#     print("Login sucessful")
# else:
#     print("login failed")


#range
# a=range(5)
# print(list(a))

#for loop
# a=[24,52,53,98,27]
# for i in a:
#     print(f"{i} is even" if i%2==0 else f"{i} is odd")

#while 
# a=int(input("Enter amount:"))
# while a>=20:
#     print("Your are exceding the limit")
# a+=2

#def
# def gretting():
#     return "hello world"
# print(gretting())

#Bmi calculator
# name=input("enter name:")
# dep=input("enter branch:")
# a=float(input("enter weight:"))
# b=float(input("enter height:"))
# bmi=a/(b**2)
# print("Your name is",name)
# print("Your branch is",dep)
# print("Your bmi value is:",bmi)
# if bmi<=25:
#     print("Your normal weight")
# else:
#     print("your over weight")

#Expressions
# x=y=z=25
# a=(x+y)*z
# b=x**2
# print(a)
# print(b)


#area of triangle
# height=int(input("enter height:"))
# base=int(input("enter base:"))
# area=0.5*base*height
# print("Area of triangle:",area)

