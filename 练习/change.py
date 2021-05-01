def changeNum1AndNum2(num1, num2):
    temp = num1
    num1 = num2
    num2 = temp
    return (num1, num2)

num1=input("请输入第一个值：")
num2=input("请输入第二个值：")
num1,num2=changeNum1AndNum2(num1,num2)
print(num1,num2)