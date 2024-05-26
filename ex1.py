# 1
names_lst = [name.strip() for name in open('names.txt', 'r')]
print(max([name for name in names_lst]))

# 2
names_lst = [name.strip() for name in open('names.txt', 'r')]
print(sum([len(name) for name in names_lst]))

# 3
names_lst = [name.strip() for name in open('names.txt', 'r')]
print("\n".join([name for name in names_lst if len(name) == len(min(names_lst, key=len))]))

# 4
names_lst = [name.strip() for name in open('names.txt', 'r')]
len_file = open("name_length.txt", "w")
len_file.writelines([str(len(name)) + "\n" for name in names_lst])

# 5
names_lst = [name.strip() for name in open('names.txt', 'r')]
input_len = int(input("Enter name length: "))
print("\n".join([name for name in names_lst if len(name) == input_len]))