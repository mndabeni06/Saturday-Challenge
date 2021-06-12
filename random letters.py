import random, string

my_list = []
for x in range(5):
    my_letter = random.choice(string.ascii_uppercase)
    my_list.append(my_letter)
    if my_letter not in my_list:
        my_list.append(my_letter)
    else:
        x = x-1


print(my_list)
