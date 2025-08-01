N = int(input("Enter the Number : "))

conv_to_str = str(N)

if conv_to_str == conv_to_str[::-1]:
    print(True)
else:
    print(False)
