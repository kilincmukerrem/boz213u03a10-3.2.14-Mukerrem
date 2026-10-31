blocks = int(input("Enter the number of blocks:"))
height = 0
blocks_in_rows = 1

while blocks > blocks_in_rows:
    blocks -= blocks_in_rows
    blocks_in_rows += 1
    height += 1


print("The height of the pyramid:" , height)
