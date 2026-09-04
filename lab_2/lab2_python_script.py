# Part 1: Take the following list and multiply all list items together.
part1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]

product = 1     # I started my variable with 1 for multiplication because 0 would make everything 0.

for num in part1:
    product = product * num     # The 'for' loop will multiply all the numbers in the part1 array

print("The final product for part1 is: ", (product))     # Prints the total

# Part 2: Take the following list and add all list items together.
part2 = [-1, 23, 483, 8573, -13847, -381569, 1652337, 718522177]

total = 0       # Now I started with 0 since we are adding. Total keeps a running total

for num in part2:
    total = total + num   # The for loop adds all the numbers in the array

print("\nThe total sum for part2 is: ", (total))

# Part 3: Add only even numbers from the list
part3 = [146, 875, 911, 83, 81, 439, 44, 5, 46, 76, 61, 68, 1, 14, 38, 26, 21] 

total = 0       # Started with zero because we are adding

for num in part3:
    if num % 2 == 0:
        total = total + num     # After isEven returns even numbers, they are all added together

print("\nThe total sum of even numbers in part3 is: ", (total))