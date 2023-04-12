name = str(input("Enter name: "))
new = []
separator = ""

for i in name:
    if i == " ":
        new.append(i.replace(' ', '%20'))
    else:
        new.append(i)

s = separator.join(new)
print(s)