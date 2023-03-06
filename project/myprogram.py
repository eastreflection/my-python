import calculator.cal

print("MAIN MENU\n")
print("press 1 for addition\n")
print("press 2 for subtraction\n")
print("press 3 for multiplication\n")
print("press 4 for division\n")

while True:
    enter=int(input("Enter your choice:"+" "))
    x=int(input("Enter 1st number:"+" "))
    y=int(input("Enter 2nd number:"+" "))
    if enter==1:
        r=calculator.cal.add(x,y)
        print("Addition of these numbers is", r)
    elif enter==2:
        r=calculator.cal.sub(x,y)
        print("Subtraction of these numbers is", r)
    elif enter==3:
        r=calculator.cal.mul(x,y)
        print("Multiplication of these numbers is", r)
    elif enter==4:
        r=calculator.cal.div(x,y)
        print("Division of these numbers is", r)
    else:
        print("Reselect the option")
    z=input("Do you want to close YES/NO")
    if z=="YES"+" ":
     break
