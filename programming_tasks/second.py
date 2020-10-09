last_names = []

while True:
    print("Type 'quit' to stop inputting last names.")
    last_name = input("Please enter a last name: ")
    if last_name == 'quit':
        break
    last_names.append(last_name)

print(f"{len(last_names)} names")

number = 1
for name in last_names:
    short_version = name[:4]
    print(f"{name:<12} {short_version}{str(number).zfill(2)}")
    number += 1
