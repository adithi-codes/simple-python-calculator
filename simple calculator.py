while True:
    operators = input("Enter any one operator (+,-,*,/,**,%, or type EXIT to stop:")

    if operators.upper() == "EXIT":
        print("Calculator is now closed!")
        break
    num1 = float(input("Enter number 1:"))
    num2 = float(input("Enter number 2:"))

    if operators == "+":
        print(num1+num2)
    elif operators == "-":
        print(num1-num2)
    elif operators == "*":
        print(num1*num2)
    elif operators == "/":
        print(num1/num2)
    elif operators == "**":
        print(num1**num2)
    elif operators == "%":
        print(num1%num2)
    else : 
        print("INVALID OPERATOR")

    