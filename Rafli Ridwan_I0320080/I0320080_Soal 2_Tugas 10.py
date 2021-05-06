import os

print("===========================")
print("===== Program Biodata Diri ")
print("===========================")

# membuka file
print("Pilih salah satu angka dibawah ini : ")
print("1. Membuat data")
print("2. Menambahkan data")
n = int(input("Masukkan pilihan (1/2) : "))

if (n == 1):
    os.system("cls")
    data_file = open("file_biodata.txt", "w")

    # menyimpan input dalam variabel
    nama = str(input("Masukkan nama : "))
    nim = str(input("Masukkan NIM : "))
    umur = int(input("Masukkan umur : "))
    status = str(input("Masukkan pekerjaan : "))
    alamat = str(input("Masukkan alamat : "))

    # mengisi variabel baru untuk file
    biodata = "Nama\tNIM\t\t\tUmur\t\tStatus\t\tAlamat"
    isi = f"\n{nama}\t{nim}\t{umur} Tahun\t{status}\t{alamat}"

    # menulis teks
    data_file.write(biodata)
    data_file.write(isi)

    # menutup file
    data_file.close()

elif (n == 2):
    os.system("cls")
    data_file = open("file_biodata.txt", "a")

    # menyimpan input dalam variabel
    nama = str(input("Masukkan nama : "))
    nim = str(input("Masukkan NIM : "))
    umur = int(input("Masukkan umur : "))
    status = str(input("Masukkan pekerjaan : "))
    alamat = str(input("Masukkan alamat : "))

    # mengisi variabel baru untuk file
    isi = f"\n{nama}\t{nim}\t{umur} Tahun\t{status}\t{alamat}"

    # menulis teks
    data_file.write(isi)

    # menutup file
    data_file.close()

else:
    print("input data yang salah")
