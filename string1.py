str1="Hello Mr Johhny Teri pant badi sohni teri pant te lagga aata tera saara kaccha patta."
print(str1[1])
str2=str1.split(" ")
print(str2)
print(type(str2))
str3=max(str2,key=len)
print(str3)

print(len(str3))
str2.remove(str3)
print(str2)

