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