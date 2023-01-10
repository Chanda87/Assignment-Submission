rows = int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(i+1):
        print("* ", end="")
    print("\n")
for i in range(rows, 0, -1):
    for j in range(0, i):
        print("* ", end=" ")

    print("\n")