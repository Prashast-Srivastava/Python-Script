# nested loop = it's the concept of having loop in a loop
#               The "inner loop" will finish all of its iteration before
#                finishing one iteration of the "outer loop".


rows = int(input("How many rows?? "))
columns = int(input("How many columns?? "))
symbol = input("Enter symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol,end="")
    print()
