# list_array = [1,2,3]

# for i in list_array:
#     print("array", i )

# print("array",list_array[0])

# for i in range(0,len(list_array)) :
#     print ("list_array", list_array[i])

# list_1 = [10, 70, 20, 40, 80]

# for i, v in enumerate(list_1):
#     print("index:", i, "elem:", v)


# print("array index satu dan seterusnya", list_1[1:])
# print("array index satu dan seterusnya", list_1[2:4])

# matrix = [
#     [0, 1, 0, 1, 0],
#     [1, 1, 1, 0, 0],
#     [89, 0, 0, 1, 1],
#     [0, 1, 1, 1, 0],
# ]

# for row in matrix:
#     for cel in row:
#         print(cel, end=" ")
#     print()

# print ("matrix", matrix[2][0])

new_list = [90,80,"aku"]
n = "aku"
if n in new_list :
    print("ada")
else :
    print("gada")
for x in new_list :
    if x == 90 :
        print("ada")
        break
    else:
        print("ga ada")

new_list.append("dia")
new_list.insert (2, "coba")
new_list.pop()
new_list.remove(90)
print(new_list)

#list comprehensive

seq = []
seq2 = []
seq3 = []
for x in range(1,50):
    if x % 2 == 0 :
        seq.append(x)
    else :
        seq2.append(x)

    if x % 7 == 0 :
        seq3.append(x)

print(seq)
print(seq2)
print(seq3)