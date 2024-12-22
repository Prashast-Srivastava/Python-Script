# nested function call = function calls inside other function calls
#                        innermost function calls are resolved first
#                        returned value is used as argument for the next function

# num = input("enter a pos. no.: ")
# num = float(num)
# num = abs(num)
# num = round(num)
# print(num)

print(round(abs(float(input("enter a whole pos. no.: ")))))
