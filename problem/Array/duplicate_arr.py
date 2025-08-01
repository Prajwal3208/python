# def find_duplicates(arr):
#     seen = set()
#     duplicates = set(x for x in arr if x in seen or seen.add(x))
#     return list(duplicates)

# print(find_duplicates([1, 2, 3, 4, 2, 3]))  # Output: [2,


arr=[1,2,3,4,2,3]
seen = set()
duplicate = set()

for x in arr:
    if x in seen:
        duplicate.add(x)
    else:
        seen.add(x)
print(duplicate)