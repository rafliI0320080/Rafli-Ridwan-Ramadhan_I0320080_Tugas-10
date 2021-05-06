import os

print("==================================")
print("===== Program Edit Direktori =====")
print("==================================")

# membuka file
print("Pilih salah satu angka dibawah ini : ")
print("1. Membuat direktori baru")
print("2. Mengganti nama direktori")
print("3. Menghapus direktori")
n = int(input("Masukkan pilihan (1/2/3) : "))

if (n == 1):
    os.system("cls")
    nama_direktori = str(input("Masukkan nama direktori : "))


    def main():
        os.mkdir(nama_direktori)


    ifname = "main"

    main()

elif (n == 2):
    nama_lama = str(input("Masukkan nama lama direktori : "))
    nama_baru = str(input("Masukkan nama baru direktori : "))


    def main():
        os.rename(nama_lama, nama_baru)


    ifname = "main"

    main()

elif (n == 3):
    hapus = str(input("Masukkan nama direktori yang akan dihapus : "))


    def main():
        os.rmdir(hapus)


    ifname = "main"

    main()

else:
    print("Input anda salah")

# direktori awalnya bernama "Biodata_prokom"
# lalu dimulai dengan pembuatan file .txt dan diisi biodata Rafli
# dilanjutkan dengan append biodata Vizal
# direktori diganti nama dari "Biodata_prokom" menjadi "Tugas 10_Biodata"