def print_params(a = 1, b = "stroka", c = True): # Задание 1
    print(a, b, c)
print_params(a = 5, b = "simbl")
print_params(c = False)
print_params(b = 25)
print_params(c = [1, 2, 3])

values_list = [1, [4, 6, "Act"], True]            # Задание 2
values_dict = {"a":11, "b":"VPN", "c": False}
print_params(*values_list)
print_params(**values_dict)

values_list_2 =[54.32, "строка"]
print_params(*values_list_2, 42)

















