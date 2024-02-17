ask_num = int(input("Please, type in a 4-digit number: "))

first_pair, second_pair = divmod(ask_num, 100)
first_num, second_num = divmod(first_pair, 10)
third_num, fourth_num = divmod(second_pair, 10)

print(first_num)
print(second_num)
print(third_num)
print(fourth_num)
