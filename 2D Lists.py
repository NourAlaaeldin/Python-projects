number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

#accessing first element in first list
print(number_grid[0][0])
#accessing first element in second list
print(number_grid[1][0])
#accessing first element in third list
print(number_grid[2][0])
#accessing first element in fourth list
print(number_grid[3][0])

print("*********************************")

#we can also loop inside the 2D list
for row in number_grid:
    for col in row:
        print(col)