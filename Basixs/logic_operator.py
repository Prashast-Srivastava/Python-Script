# logical opertors (and,or,not) = used to check if one or more conditional statements are true

temp = int(input("what is the temperature outside? "))

if not(temp >= 0 and temp <= 30):
    print("temperature is bad today")
    print("stay inside")

elif not(temp < 0 or temp > 30):
    print("the temperature is good today")
    print("go outside")

