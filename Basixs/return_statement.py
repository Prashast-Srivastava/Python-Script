# return statement = functions send Python values/objects back to the caller.
#                    These values/objects are known as the function's return value..

def product(number1,number2):
    result = number1 * number2
    # return number1*number2
    return result
def main():
    num1 = int(input("enter 1st no.: "))
    num2 = int(input("enter 2nd no.: "))
    print(product(num1,num2))

main()