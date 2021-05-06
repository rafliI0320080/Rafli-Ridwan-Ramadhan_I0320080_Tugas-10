print("Selamat datang di Program Biodata")
print("=================================")

#ambil input dari user
nama = str(input("Nama : "))
umur = str(input("Umur : "))
alamat = str(input("Alamat : "))

#format teks
teks = f"Nama : {nama}\nUmur : {umur}\nAlamat : {alamat}\n"

#buka file untuk ditulis
file_bio = open("biodata.txt", "w")

#tulis teks ke file
file_bio.write(teks)

#tutup file
file_bio.close()