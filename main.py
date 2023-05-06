# 1).

x = {6, 9, 30, 60}
y = {10, 15, 20, 60}


def update_func():
    print(x & y)


update_func()

# 2).
x = "sims"
y = "s"


def find_func():
    return x.find("s", 2)


print(find_func())

# 3).

x = input("Input str:")


def func_capital():
    return x.capitalize() + "."


print(func_capital())

# 4).

name = input("Input name:")
age = int(input("Input age:"))


def name_age(name, age):
    return f"Hi. My name is {name} and Im {age} years old"


print(name_age(name, age))
