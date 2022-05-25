# Author: SMR (AMDG) 05/17/22

# addition
def add ():
    print("Addition")
    n = float(input("Enter the number: "))
    t = 0 
    ans = 0
    while n != 0:
        ans = ans + n
        t+=1
        n = float(input("Enter another number (0 to calculate): "))
    return [ans,t]

# subtraction
def sub ():
    print("Subtraction");
    n = float(input("Enter the number: "))
    t = 0 
    sum = 0
    while n != 0:
        ans = ans - n
        t+=1
        n = float(input("Enter another number (0 to calculate): "))
    return [ans,t]
# multiplication
def mult ():
    print("Multiplication")
    n = float(input("Enter the number: "))
    t = 0 
    ans = 1
    while n != 0:
        ans = ans * n
        t+=1
        n = float(input("Enter another number (0 to calculate): "))
    return [ans,t]

# Avg
def average():
    an = []
    an = add()
    t = an[1]
    a = an[0]
    ans = a / t
    return [ans,t]

"main code for actually calculating"
while True:
    list = []
    print(" My first python program!")
    print(" Simple Calculator in python by Malik Umer Farooq")
    print(" Enter 'a' for addition")
    print(" Enter 's' for substraction")
    print(" Enter 'm' for multiplication")
    print(" Enter 'v' for average")
    print(" Enter 'q' for quit")
    c = input(" ")
    if c != 'q':
        if c == 'a':
            list = add()
            print("Ans = ", list[0], " total inputs ",list[1])
        elif c == 's':
            list = sub()
            print("Ans = ", list[0], " total inputs ",list[1])
        elif c == 'm':
            list = mult()
            print("Ans = ", list[0], " total inputs ",list[1])
        elif c == 'v':
            list = average()
            print("Ans = ", list[0], " total inputs ",list[1])
        else:
            print ("Sorry, invilid character")
    else:
        break
