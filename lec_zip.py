names = ['John', 'David', 'Maria', 'Anna']
ages=[16, 25, 19, 15]
is_teenager = [True, False, True, False]

users = list(zip(names,ages,is_teenager))
print(users)

print("User age:", dict(zip(names, ages)))