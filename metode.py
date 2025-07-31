# # def pertambahan (a,b) :
# #     return a+b 

# # def pengurangan (a,b):
# #      return a-b

# # def perkalian (a,b) :
# #      return a*b

# # def pembagian (a,b) :
# #      if b == 0:
# #           return "tidak bisa dibagi 0"
# #      return a/b
# data = input("masukan angka operasi dan angka").split()

# operator = data[0]
# angka_list = list(map(float, data[1:]))


# def pertambahan(angka_list):
#     return sum(angka_list)


# def pengurangan(angka_list):
#     hasil = angka_list[0]
#     for angka in angka_list[1:]:
#      hasil -= angka 
#     return hasil 

# def perkalian(angka_list):
#    hasil_perkalian = angka_list [0]
#    for angka in angka_list[1:]:
#       hasil_perkalian *= angka
#    return hasil_perkalian    

# def pembagian (angka_list):
#    hasil_pembagian = angka_list [0]
#    for angka in angka_list[1:]:
#       hasil_pembagian /= angka
#    return hasil_pembagian

# if operator == "+":
#    print(pertambahan(angka_list))
# elif operator == "-":
#    print(pengurangan(angka_list))
# elif operator == "*":
#    print(perkalian(angka_list))
# elif operator == "/":
#    print(pembagian(angka_list))
# else:
#  print("operator tidak dikenal")

print(eval(input("")))


