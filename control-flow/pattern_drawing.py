row = int(input("Enter the size of the pattern:"))
while row <= 0:
    row= int (input("Enter a positive integer:"))
for _ in range(row):
 print("*", end="")