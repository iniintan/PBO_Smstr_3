# Inisialisasi list untuk menyimpan data mahasiswa
mahasiswa_list = []

# Input jumlah mahasiswa
jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa: "))

# Input data mahasiswa
for i in range(jumlah_mahasiswa):
    nim = input("Masukkan NIM mahasiswa (empat digit terakhir): ")
    nama = input("Masukkan nama mahasiswa: ")
    fakultas = input("Masukkan fakultas mahasiswa: ")

    # Menambahkan data mahasiswa ke list
    mahasiswa_list.append({"NIM": nim, "Nama": nama, "Fakultas": fakultas})

# Melakukan sorting berdasarkan NIM
mahasiswa_list.sort(key=lambda x: x["NIM"])

# Menampilkan hasil sorting
print("\nHasil Sorting Berdasarkan NIM:")
for mahasiswa in mahasiswa_list:
    print(f"NIM: {mahasiswa['NIM']}, Nama: {mahasiswa['Nama']}, Fakultas: {mahasiswa['Fakultas']}")