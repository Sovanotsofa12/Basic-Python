import metode

def nama() :
    print("andrew")
    for i in range (5):
        print (i)

nama()
nama()
nama()

def penjumlahan(a,b):
    return a + b 

print("hasil penjumlahan", penjumlahan(5,6))

def mencariluaslingkaran(r : int):
    return 3.14 * r ** 2

print("hasil luas lingkaran", mencariluaslingkaran(7)) 

def perkalian(a,b):
    nama = 'Andrew'
    print("hasil",(a * b))

penjumlahan(2,3)
(penjumlahan(43,789))

perkalian(3,4)

def user(username:str,age:int,email:str,password:str):
    if isinstance(username, str):
        print("username must be string")
    if isinstance(age, int):
        print("age must be int")
    if isinstance(email, str):
        print("email must be str")
    if isinstance(password, str):
        print("password must be string")
    return {
        "username": username,
        "age": age,
        "email": email,
        "password": password
    }

user1 = user("abc", 42 ,"daksjd@gmail.com","123456789")
user2 = user(age=32, username= "asdf" ,password="123456789",email="ahdjsad@gmail.com")
user3 = user(32,"abc","askgjdhajkhda@gmail.com","12345678")



print(user1)
print(user2)
print(user3)

def penjumlahan_1 (*numbers):
    total = 0 
    for number in numbers :
        total += number
        print(f'{number} + {total}')
    print (total)
penjumlahan_1(1,2,3,4)

x = metode.pembagian (10,3)
print(x)

angka1 = float(input("angka pertama"))
angka2 = float(input("angka kedua"))
operator = input("opsi aritmatika (x,/,+,-)")
if operator =="+":
   a = metode.pertambahan(angka1,angka2)

elif operator =="-":
   a = metode.pengurangan(angka1,angka2)

elif operator =="x":
   a = metode.perkalian(angka1,angka2)

elif operator =="/":
    a = metode.pembagian(angka1,angka2)

else : 
    print("symbol tidak sesuai")
    
print (a)





