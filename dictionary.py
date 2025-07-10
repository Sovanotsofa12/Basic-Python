profile = dict(
    nama = "andrew",
    umur = 18 ,
    alamat = "GKI" 
)

profile2 = {
    "nama": "andrew",
    "umur" : 18 ,
    "alamat" : "GKI"
}

print(profile)
print(profile2)

for key in profile2:
    print (f"{key} adalah {profile2[key]}")

profile2["sekolah"] = "sma bruderan pwt"

print(profile2)

profile2.pop("umur")
print (profile2)

