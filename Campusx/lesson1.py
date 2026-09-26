

import math


def task1():
    "Q1 :- Print the given strings as per stated format."
    print("Data", "Science", "Mentorship", "Program", "By", "CampusX", sep="-")

def task2():
    " Write a program that will convert celsius value to fahrenheit."
    celsius = 25
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C is equal to {fahrenheit}°F")

def task3():
    "Q3:- Take 2 numbers as input from the user.Write a program to swap the numbers without using any special python syntax."
    num1= int(input("Enter first number: "))
    num2= int(input("Enter second number: "))
    print("Before swapping: num1 =", num1, "num2 =", num2)
    num1, num2 = num2, num1
    print("After swapping: num1 =", num1, "num2 =", num2)

def task4():
    "Q4:- Write a program to find the euclidean distance between two coordinates.Take both the coordinates from the user as input."
    x1 = float(input("Enter x-coordinate of first point: "))
    y1 = float(input("Enter y-coordinate of first point: "))
    x2 = float(input("Enter x-coordinate of second point: "))
    y2 = float(input("Enter y-coordinate of second point: "))
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    print(f"The Euclidean distance between ({x1}, {y1}) and ({x2}, {y2}) is {distance}")

def task5():
    "Write a program to find the simple interest when the value of principle,rate of interest and time period is provided by the user."
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the rate of interest: "))
    time = float(input("Enter the time period: "))
    simple_interest = (principal * rate * time) / 100
    print(f"The simple interest is {simple_interest}")

# heads 10
# legs 28
def task6():
    "Q6:- Write a program that will tell the number of dogs and chicken are there when the user will provide the value of total heads and legs."
    heads= int(input("Enter the total number of heads: "))
    legs= int(input("Enter the total number of legs: "))
    dogs= (legs -(2 * heads))//2
    chickens= heads- dogs
    print(f"Number of dogs: {dogs}")
    print(f"Number of chickens: {chickens}")





# task1()  # Output: Data-Science-Mentorship-Program-By-CampusX
# task2()  # Output: 25°C is equal to 77°F
# task3()  # Output: Swapped values of the two numbers
# task4()  # Output: The Euclidean distance between two coordinates
# task5()  # Output: The simple interest is {simple_interest}