name = input ('Enter your first name and last name: ')
name_list = name.split(' ')
name_list.reverse()
name_str = " ".join(name_list)
print(name_str)
