# READING A FILE

# f = open('myfile.txt', 'r')
# # print(f)
# text = f.read()
# print(text)
# f.close()

# WRITING A FILE

# f = open('myfile.txt', 'a')
# f.write('Hello, world!')
# f.close()

# with open('myfile.txt', 'a') as f:
#   f.write("Hey I am inside with")
# f = open("prajwal.txt","r")
# content = f.read()
# print(content)
# f.close()

f = open('prajwal.txt','a')
f.write("kjsdkjjflkhfjbkfjlkfkjfkjdhljhsjglkdjfhkcnkjhchjbckj jfkjhdgfjh f gsjhdgfj" )
# # f.write("helloo  guys")
f=open('prajwal.txt','r')
c = f.read()
print(c)
f.close()
