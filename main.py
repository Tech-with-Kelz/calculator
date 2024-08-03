# Python program for simple calculator

# Function to add two numbers
def add( x, y):
  return x + y

# Function to subtract two numbers
def subtract( x, y):
  return x - y

# Function to multipy two numbers
def multiply( x, y):
  return x * y

# Function to divide two numbers
def divide( x, y):
  if y != 0:
    return x / y
  else:
    return "Error! division by zero"

print("select an operation: \n" \
     "1. Add\n" \
     "2. Subtract\n" \
     "3. Multiply\n" \
     "4. Divide\n")
 while True:
        choice = input("Enter choice (1/2/3/4): ")

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                result = divide(num1, num2)
                if result == "Error! Division by zero.":
                    print(result)
                else:
                    print(f"{num1} / {num2} = {result}")

            next_calculation = input("Do you want to perform another calculation? (yes/no): ")
            if next_calculation.lower() != 'yes':
                break
        else:
            print("Invalid Input")

if __name__ == "__main__":
    calculator()



