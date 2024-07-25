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
  
