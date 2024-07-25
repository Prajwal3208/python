try:
  a = int(input("Enter a number between 5 and 9: "))

  if 5 < a < 9:
      print(a * a)
  else:
      raise ValueError("The number entered is not between 5 and 9")
except Exception as e:
  print(e)
finally:
  print("Thank you")


#quick quiz



try:
  
  
  a = input("Enter a number between 5 and 9 or 'quit' : ")
  if a == "quit":
  #if a.lower() == "quit": ##for convert upper to lower
    print("quit")

  else:
    a = int(a)
    if (5 < a < 9):
      print((a * a))
    else:
      raise ValueError("The number entered is not between 5 and 9")
except Exception as e :
  print(e)
  print("Enter the integer only in between 5 to 9")
  

finally:
  print("Thank you")
