# P2: Simple Calculation

print("\n--- Simple Calculator ---\n")
a = int(input("Enter the number for a: "))
b = int(input("Enter the number for b: "))

while True:
  print("\n----- OPERATIONS -----")
  print("1. Addition")
  print("2. Subtraction")
  print("3. Multiplication")
  print("4. Division")
  print("5. Exit")
  
  choice = int(input("Enter the number for choice: "))
  
  match choice:
    case 5:
      print("\nThanks for using Simple Calculator! \n")
      break
    
    case 1:
      c = a + b
      print("Addition is:", c)

    case 2:
      c = a - b
      print("Subtraction is:", c)

    case 3:
      c = a * b
      print("Multiplication is:", c)

    case 4:
        if b == 0:
            print("Error: Cannot divide by zero")
        else:
            c = a / b
            print("Division is:", c)

    case _:
        print("Invalid choice")
