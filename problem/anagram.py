str1= "prajwal"
str2 = "prawjal"

str01 = str1.replace(' ','').lower()
str02 = str2.replace(' ','').lower()

s1 = sorted(str01)
s2 = sorted(str02)

print(s1==s2)
