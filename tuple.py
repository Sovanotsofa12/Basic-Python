new_tuple = (23,40,"andrew", True)

# print(new_tuple)
# print("panjang tuple", len(new_tuple))
# print(new_tuple[2])

# for x in range (0, len(new_tuple)) :
#     print(f"tuple index {x} isinya adalah {new_tuple[x]}")
#     print("tuple index %s" %x + "isinya adalah %s" %(new_tuple[x]))

for x, y in enumerate (new_tuple) :
     print(f"tuple index {x} isinya adalah {y}")