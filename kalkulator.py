while True:
   print("Options:")
   print("Enter 'add' to add two numbers")
   print("Enter 'subtract' to subtract two numbers")
   print("Enter 'multiply' to multiply two numbers")
   print("Enter 'divide' to divide two numbers")
   print("Enter 'quit' to end the program")
   user_input = input(": ")

   if user_input == "quit":
      break
   elif user_input == "add":
      print('please, write first number: ')
      first_number=input()
      print('please, write second number: ')
      second_number=input()
      print('result:')
      print(float(first_number)+float(second_number))
   elif user_input == "subtract":
      print('please, write first number: ')
      first_number=input()
      print('please, write second number: ')
      second_number=input()
      print('result:')
      print(float(first_number)-float(second_number))
   elif user_input == "multiply":
      print('please, write first number: ')
      first_number=input()
      print('please, write second number: ')
      second_number=input()
      print('result:')
      print(float(first_number)*float(second_number))
   elif user_input == "divide":
      print('please, write first divided number: ')
      first_number=input()
      print('please, write divisor: ')
      second_number=input()
      while (float(second_number))==0:
            print ("You can not divide by zero. Plase, choose another divisor.")
            second_number=input()
      print('result:')
      print(float(first_number)/float(second_number))
     
   else:
      print("Unknown input")