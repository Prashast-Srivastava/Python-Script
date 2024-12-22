# if statement = a block of code which executes when it's condition is true

age = int(input("enter your age: "))

if age > 18:
    print("eligible to give vote")
elif age < 18:
    print("not eligible to give vote")
else :
    print("you can apply for voter card")
