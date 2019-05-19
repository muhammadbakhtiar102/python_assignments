Name =(input("Please enter your name"))
print("Welcome Mr."+ Name.upper() + "\n " "To the four operator Calculator")
print("here you can use these four operator to calculte \n / Divide \n * Multiply \n + Addition \n - Substract")
Num1 =(float(input("Enter First Digit")))
Oprt =(input("Select operator"))
Num2 =(float(input("Enter Second Digit")))
if Oprt == "+":
    ans =(Num1+Num2)
    print("Your Result is \n",ans)
elif Oprt == "-":
    ans =(Num1-Num2)
    print("Your Result is \n",ans)
elif Oprt == "*":
    ans=(Num1*Num2)
    print("Your Result is \n",ans)
elif Oprt == "/":
    ans=(Num1/Num2)
    print("Your Result is \n",ans)
else:
    print("syntax error!")
print("***End***")