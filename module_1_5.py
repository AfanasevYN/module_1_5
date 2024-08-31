immutable_var = ("топор", 5, "артерия", 2, "календарь", 3, "спорт", True)
print(immutable_var)
#immutable_var[0] = "нож"
#TypeError: 'tuple' object does not support item assignment
mutable_list = ["топор", 5, "артерия", 2, "календарь", 3, "спорт", 1]
print(mutable_list)
mutable_list[7] = 'понял'
print(mutable_list)


