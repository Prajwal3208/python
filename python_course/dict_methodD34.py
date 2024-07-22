# ep1 = {122: 45, 123: 89, 567: 69, 670: 69}
# ep2 = {222: 67, 566: 90}

# # ep1.update(ep2)
# # ep1.clear()
# # ep1.pop(122)
# ep1.popitem()
# del ep1[122]
# print(ep1) 


# dict = {'name':"prajwal","age":19,}
# print(dict)
# dict.update({"name":"kadam"})
# print(dict)
# dict.clear()
# print(dict)
# info = {'name':'Karan', 'age':19, 'eligible':True}
# info.pop('eligible')
# print(info)

info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
info.popitem()
print(info)
del info["age"]
print(info)
del info
print(info)
