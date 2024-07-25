def encode(message):
  if len(message) <= 2:
    message_revers = message[::-1]
    print(message_revers)
  else:
    new_msg = message[1:] + message[0]
    return "THE DECODED MSG IS :", "xyz" + new_msg + "abc"
    

def decode(message):
    if len(message) <= 2:
      message_revers = message[::-1]
      print(message_revers)
    else:
      new_msg = message[3:-3]
      return "THE ORIGINAL MSG IS :",(new_msg[-1] + new_msg[:-1])

option = int(input("Enter 1 for encode and 2 for decode: "))

print(option)
message = input("Enter the msg str only : ")
if option == 1:
  print(encode(message))
elif option == 2:
  print(decode(message))
else:
  print("invalid input ")
  

