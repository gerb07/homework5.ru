immutable_var = ('banana', 'apple', 'coconut', 13)
print(immutable_var)
print(immutable_var[0])
print(immutable_var[0:3:2])
#immutable_var[0] = ('hotdog')   #нельзя, потому что тип кортеж,не изменяется

mutable_list = ['dog', 'cat', 'elephant']
print(mutable_list[0])
mutable_list[0] = 'giraffe'
print(mutable_list)




