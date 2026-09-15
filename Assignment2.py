# salary=int(input("enter the salary"))

# if salary<30000:
#     print("5% tax and and tax amt will be ", (5*salary)/100)
# elif salary >=30000 and salary <=70000:
#     print("15 % tax and the tax amt will be ",(15*salary)/100)
# else:
#     print("25 % tax and the tax amt will be ",(25*salary)/100)


# def nums_in_range(a,b):
#     for i in range(a,b+1):
#         if i%2==0:
#             print(i)

# nums_in_range(6,16)


# def digits_of_number(n):
#     for i in n:
#         print(i)

# digits_of_number("458")

# def digi_of_num(n):
#     while n>0:
#         print(int(n%10))
#         n=int(n/10)

# digi_of_num(548)

# count the numberof digits in the number n
# def num_of_digits(n):
#     count=0
#     n=abs(n)

#     if n==0:
#         return 1

#     while n>0:
#         count+=1
#         n//=10 
#     return count

# print(num_of_digits(548762))


# def sum_of_digit(n):
#     sum=0
#     while n>0:
#         sum+=int(n%10)
#         n=int(n/10)
#     return sum

# print(sum_of_digit(4578))


# write a program to print all the numbers that is divisible by both 3 and 5
# for i in range(1, 101):
#     if i%3==0 and i%5==0:
#         print(i)




# n=input("enter the number")
# while True:
#     n=input("enter the number")
    
#     if n=="quit":
#         break

#     n=int(n)
#     if n>0:
#         print("positive")
#     else:
#         print("negative")


# def calculator(a,b,operation):
#     match operation:
#         case "+":
#             print(a+b)
#         case "-":
#             print(a-b)
#         case "*":
#             print(a*b)
#         case "/":
#             print(a/b)
#         case _:
#             print("invalid operation")


# calculator(4,6,"*")




# def is_prime(n):
#     for i in range(2,n):
#         if n%i ==0:
#             return False
#     return True

# print(is_prime(13))


# number guessing game
def guess_game():
    search=input("enter the number to search")
    while True:
        n=input("enter the number")

        if n==search:
            print("you guess correct")
            break
        elif n<search:
            print("Too low")
        else :
            print("Too high")

guess_game()