from abc import ABC, abstractmethod
import math
class BankAccount:
    def __init__(self, account_no, owner_name , balance):
        self.account_no=account_no
        self.owner_name=owner_name
        self.__balance=balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, new_balance):
        self.balance=new_balance

    def deposit(self,amount):
        self.__balance=self.__balance+amount

    def withdraw(self,amount):
        self.__balance=self.__balance-amount
    


acc1=BankAccount(123,"abhishek",100_000)

print(acc1.owner_name)
print(acc1.get_balance())
acc1.deposit(5000)
print(acc1.get_balance())
acc1.withdraw(50000)
print(acc1.get_balance())



# print(acc1._BankAccount__balance)


class Book:
    def __init__(self,title, author, reviews=[]):
        self.title=title
        self.author=author
        self.reviews=reviews

    def add_new_review(self,review):
        self.reviews.append(review)

    def count_reviews(self):
        return len(self.reviews)

    def display_reviews(self):
        for i in self.reviews:
            print(i)


b1=Book("ramayan","vedvyas",["very good", "excellent"])
print(b1.reviews)
b1.add_new_review("awesome")
print(b1.reviews)
print(b1.count_reviews())
b1.display_reviews()


class Student:
    def __init__(self, name , roll_no, marks):
        self.__name=name 
        self.__roll_no=roll_no
        self.__marks=marks

    # getters
    def get_name(self):
        return self.__name
    def get_roll_no(self):
        return self.__roll_no
    def get_marks(self):
        return self.__marks


    # setters
    def set_name(self,new_name):
        if new_name!="":
            self.__name=new_name
        else:
            print("new name cannot be empty")
    def set_roll_no(self,new_roll_no):
        if 1 <=new_roll_no <=100:
            self.__roll_no=new_roll_no
        else:
            print("new rollnio should be in the between 1 and 100")

    def set_marks(self, new_marks):
        if new_marks>=0:
            self.__marks=new_marks
        else:
            print("marks cannot be negative")

# Creating object
student = Student("Abhishek", 10, 85)

# Get values
print("Name:", student.get_name())
print("Roll No:", student.get_roll_no())
print("Marks:", student.get_marks())

# Update values
student.set_name("Rahul")
student.set_roll_no(20)
student.set_marks(90)

print("\nAfter updating:")
print("Name:", student.get_name())
print("Roll No:", student.get_roll_no())
print("Marks:", student.get_marks())


class Shape:
    def area(self):
        print("calculates the area")

class Circle(Shape):
    def __init__(self, radius):
        self.radius=radius

    def area(self):
        return 3.14 *self.radius*self.radius

class Triangle():
    def __init__(self, base, height):
        self.base=base
        self.height=height
    
    def area(self):
            return (self.base*self.height)/2

class Rectangle():
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    
    def area(self):
        return self.length*self.breadth

# Creating objects
c = Circle(5)
r = Rectangle(10, 4)
t = Triangle(6, 8)

print("Circle area:", c.area())
print("Rectangle area:", r.area())
print("Triangle area:", t.area())


class Vehicle:
    def __init__(self, brand, model):
        self.brand=brand
        self.model=model

class Car(Vehicle):
    def __init__(self,seats,brand,model):
        super().__init__(brand,model)
        self.seats=seats

class Bike(Vehicle):
    def __init__(self, brand, model,engine_cc):
        super().__init__(brand, model)
        self.engine_cc=engine_cc

# Creating objects
car = Car("Toyota", "Fortuner", 7)
bike = Bike("Honda", "Shine", 125)

print("Car:")
print("Brand:", car.brand)
print("Model:", car.model)
print("Seats:", car.seats)

print("\nBike:")
print("Brand:", bike.brand)
print("Model:", bike.model)
print("Engine CC:", bike.engine_cc)



class Employee(ABC):
    @abstractmethod
    def calc_salary(self):
        pass

class Intern(Employee):
    def calc_salary(self):
        print("salary of the intern is 75000")

class FullTimeEmployee(Employee):
    def calc_salary(self):
        print("salary of the fte is 120000000")

class ContractEmployee(Employee):
    def calc_salary(self):
        print("the salary of the contract employee is 35216546541")

intern = Intern()
fulltime = FullTimeEmployee()
contract = ContractEmployee()

intern.calc_salary()
fulltime.calc_salary()
contract.calc_salary()

class Person:

    def __init__(self, name, age=None, address=None):
        self.name = name
        self.age = age
        self.address = address

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Address:", self.address)


# Name only
p1 = Person("Abhishek")

# Name + age
p2 = Person("Rahul", 21)

# Name + age + address
p3 = Person("Amit", 22, "Lucknow")

p1.display()
print()

p2.display()
print()

p3.display()


class Player:
    player_count=0

    def __init__(self,name,level):
        self.name=name
        self.level=level
        Player.player_count+=1

# Creating players
p1 = Player("Abhishek", 10)
p2 = Player("Rahul", 15)
p3 = Player("Amit", 20)

print("Player 1:", p1.name, p1.level)
print("Player 2:", p2.name, p2.level)
print("Player 3:", p3.name, p3.level)

print("Total players created:", Player.player_count)


class Herbivore:
    def eat_plant(self):
        print("eats grass")

class Carnivore:
    def eat_flesh(self):
        print("eats flesh")

class Omnivore:
    def eat_both(self):
        print("eats both")

class Bear(Herbivore,Carnivore,Omnivore):
    def show(self):
        print("bear is an omnivore animal")


bear=Bear()
bear.show()
bear.eat_both()


# class User:                                   incomplete
#     def __init__(self,name):
#         self.name=name

#     def send_msgs(self,msg)

# class Message:
#     def __init__(self,msg):
#         self.msg=msg

# class ChatRoom:
#     def __init__(self,chatroom):
#         self.chatroom=chatroom

