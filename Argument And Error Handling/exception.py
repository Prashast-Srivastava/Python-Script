# exception = events detected during execution that interrupt the flow of a program

try:
    numerator = int(input("enter the numerator: "))
    denominator = int(input("enter the denominator: "))
    result = numerator/denominator
except ZeroDivisionError as e:
    print(e)
    print("u can't divide by 0 , idiot!!")
except ValueError as e:
    print(e)
    print("enter only int no please")
except Exception as e:
    print(e)
    print("something went wrong !!!")
else :
    print(result)
finally:
    print("this will always execute")