rows = int(input("How many rows do you wish to have?"))
columns = int(input("How many columns do you wish to have?"))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol,end=" ")
    print( )