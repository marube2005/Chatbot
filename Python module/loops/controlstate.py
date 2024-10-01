#Loop Control Statements = change a loops execution from its normal sequence
#break
#continue
#pass

name =""
while len(name) == 0:
    name = input("Enter name!")
    if len(name) != 0:
        break
number = "1234-467-890"
for i in number:
    if i == "4" or i == "-":
        continue
    print(i, end="")
    print()

for i in range(1,21):
 if i == 13:
    pass
 else:
    print(i, end="")
