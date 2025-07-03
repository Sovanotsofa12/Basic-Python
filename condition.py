angka = 7
if angka == 8 :
    print("ini angka 8")
else :
    print("ini bukan angka 8")

angka_penyebut = 24
if angka_penyebut % 2 == 0 :
    print("ini angka genap")
else :
    print("ini angka ganjil")


angka_lain = 43
if angka_lain > 0 :
    print("lebih dari 0")
    if angka_lain == 46 :
        print("ini angka 46")
    else :
        print("ini bukan 46")
elif angka_lain < 0 :
    print("ini kurang dari 0")
else :
    print("angka ini bernilai 0")


data = True
if type(data) == str : 
    print("ini string")
elif type(data) == int :
    print("ini integer")
elif type(data) == bool :
    print("ini boolean")
