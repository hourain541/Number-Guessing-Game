import calculator

print("Custom Module Calculator")
print("------------------------")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nResults")
print("Addition:", calculator.add(num1, num2))
print("Subtraction:", calculator.subtract(num1, num2))
print("Multiplication:", calculator.multiply(num1, num2))
print("Division:", calculator.divide(num1, num2))
print("Value of PI:", calculator.PI)