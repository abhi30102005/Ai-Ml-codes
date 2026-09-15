# ask the user for the string and check whether it is a palindrime o not

# name=input("enter the name to check the palindrome")

# if name==name[::-1]:
#     print("it is a palindrome")
# else:
#     print("it is not the palindrome")


# list=[5,4,8,9,6]

# sum=0
# for i in list:
#     sum+=i
# avg=sum/len(list)
# print(avg)



# input two list from the user and merge them and sort tem
# list1=list(map(int,input("Enter the elements in list1").split()))
# list2=list(map(int,input("Enter the numbers in list2").split()))

# merged_list=list1+list2
# print(merged_list)
# merged_list.sort()

# print(merged_list)

# given a tuple of integers
# a tuple of all even integers

# t=tuple(map(int , input("Enter the integers").split()))

# even=tuple(x for x in t if x%2==0)
# odd=tuple(x for x in t if x%2!=0)

# print(even)
# print(odd)


# classroom={
    
# }


# choice=input("Enter the value to A B C D to manipulate the dictionary")

# if choice== "A":
#     # Add a student
#     name=input("Enter te name of the student")
#     marks=int(input("enter the marks of the student"))
#     classroom.update({name : marks})
# elif choice == 'B':
#     # update marks
#     name=input("Enter the name")
#     marks=int(input("Enter ethe marks to update"))
#     classroom[name]=marks
# elif choice=="C":
#     # search for the student
#     name =input("Enter the student name to search")
#     if name in classroom:
#         print(f"marks of {name} is {classroom.get(name)}")
#     else:
#         print("studnet does not exist")
# elif choice =="D":
#     # display all the students and the marks
#     for name , marks in classroom.items():
#         print(f"{name} : {marks} ")
    

# print(type(classroom))




# words=["apple", "banana", "kiwi", "cherry" , "'mango"]
# dict={}

# for i in words:
#     dict.update({i: len(i)})

# for fruit,length in dict.items():
#     print(f"{fruit} : {length}")

# print(dict)


# takes the string from the user and print the number of spaces
# user_string=input("Enter the string to fond teh spaces between the strings")
# count=0
# for i in user_string:
#     if i==" ":
#         count+=1

# print(count)

# list1 =[1,2,3,4]
# list2 =[5,6,7,8]

# s=set()
# for i in list1:
#     s.add(i)

# for i in list2:
#     s.add(i)

# if len(list1) +len(list2) == len(s):
#     print("share no common elements")
# else:
#     print("share common elememnts")


# list=[4,4,5,5,8,8,6,7,1,2,3]

# s= set()
# list_fin=[]

# for i in list:
#     if i in s:
#         if i not in list_fin:
#             list_fin.append(i)
#         else:
#             continue
#     else:
#         s.add(i)

# print(list_fin)


# all unique characters from the users string
user_string=input("Enter the string")
s=set()

for i in user_string:
    s.add(i)
print(s)
print(len(s))