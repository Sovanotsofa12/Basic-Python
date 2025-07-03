list_array = [1,2,3]

for i in list_array:
    print("array", i )

print("array",list_array[0])

for i in range(0,len(list_array)) :
    print ("list_array", list_array[i])

list_1 = [10, 70, 20, 40, 80]

for i, v in enumerate(list_1):
    print("index:", i, "elem:", v)


print("array index satu dan seterusnya", list_1[1:])
print("array index satu dan seterusnya", list_1[2:4])

matrix = [
    [0, 1, 0, 1, 0],
    [1, 1, 1, 0, 0],
    [89, 0, 0, 1, 1],
    [0, 1, 1, 1, 0],
]

for row in matrix:
    for cel in row:
        print(cel, end=" ")
    print()

print ("matrix", matrix[2][0])