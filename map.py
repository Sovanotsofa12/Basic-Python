angka = [ 1,2,3,4,5,6,7,8,9,10,11 ]
# hasil_kuadrat = []

# for number in angka:
#     hasil_kuadrat.append(number**2)

def kuadrat (num):
    return num ** 2

# hasil = list(map(kuadrat, angka))
hasil = [x ** 2 for x in angka]

print(hasil)

