x = range(2000,3201)
print(x)
num_list = []
for i in x :
    if i % 7 == 0 and i%5 != 0:
        num_list.append(i)

print(num_list)

name_str = ",".join(map(str,num_list))
print(name_str)


