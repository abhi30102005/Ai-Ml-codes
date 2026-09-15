# username=input("enter the username")
# password=input("enter the password")

# if (username=="admin" and password=="pass") :
#     print("login succcessfull")
# elif(username!="admin"):
#     print("invalid username")
# else:
#     print("invalid password")

# color=input("eter the color")

# match color:
#     case "Green":
#         print("Go")
#     case "Red":
#         print("Stop")
#     case "Yellow":
#         print("Look")
#     case _ :
#         print("wrong choice of color")


# multiplication table for any number n

# n=int(input("enter the value of n"))
# i=0
# while i<10:
#     print(n,"*",i+1,"=",n*(i+1))
#     i+=1


# word="artificial"
# count=0
# for ch in word:
#     if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
#         count+=1

# print("ans=",count)

# write a function to print the factorial of n
n=int(input("enter the value"))

def fact(n):
    ans=1
    while n>0:
        ans*=n
        n-=1
    return ans

print(fact(n))