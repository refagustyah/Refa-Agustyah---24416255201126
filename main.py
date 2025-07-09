import csv
from crud import (
    catat_transaksi,
    tampilkan_rekap,
    update_transaksi,
    hapus_transaksi
)
from laporan import (
    laporan_bulanan,
    laporan_tahunan
)

FILE = 'data_keuangan.csv'

def baca_data(nama_file):
    data = []
    try:
        with open(nama_file, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            data = list(reader)
    except FileNotFoundError:
        print(f"File {nama_file} tidak ditemukan, membuat yang baru...")
    return data

def tulis_data(nama_file, data):
    if not data:
        return
    fieldnames = data[0].keys()
    with open(nama_file, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

data = baca_data(FILE)

while True:
    print("\n=== Manajemen Keuangan Pribadi ===")
    print("1. Catat Pemasukkan")
    print("2. Catat Pengeluaran")
    print("3. Laporan Bulanan")
    print("4. Laporan Tahunan")
    print("5. Lihat Rekap Transaksi")
    print("6. Update Transaksi")
    print("7. Hapus Transaksi")
    print("8. Keluar")

    pilihan = input("Pilih menu (1-8): ")

    if pilihan == '1' or pilihan == '2':
        tanggal = input("Masukkan Tanggal (tgl-bln-thn): ")
        deskripsi = input("Masukkan Deskripsi (Pemasukkan/Pengeluaran): ")
        jenis = input("Masukkan Jenis: ")
        tipe = 'Pemasukkan' if pilihan == '1' else 'Pengeluaran'
        jumlah = input("Masukkan Jumlah: ")
        catat_transaksi(data, tanggal, deskripsi, jenis, tipe, jumlah)
        tulis_data(FILE, data)
        
    elif pilihan == '3':
        bulan = int(input("Masukkan Bulan (1-12): "))
        tahun = input("Masukkan tahun: ")
        laporan_bulanan(data, bulan, tahun)

    elif pilihan == '4':
        tahun = input("Masukkan tahun: ")
        laporan_tahunan(data, tahun)

    elif pilihan == '5':
        tampilkan_rekap(data)

    elif pilihan == '6':
        for idx, item in enumerate(data):
            print(f"{idx+1}. {item}")
        index = int(input("Masukkan nomor transaksi yang akan diupdate: ")) - 1
        update_transaksi(data, index)

    elif pilihan == '7':
        for idx, item in enumerate(data):
            print(f"{idx+1}. {item}")
        index = int(input("Masukkan nomor transaksi yang akan dihapus: ")) - 1
        hapus_transaksi(data, index)

    elif pilihan == '8':
        tulis_data(FILE, data)
        print("Data telah disimpan. Terima kasih telah menggunakan aplikasi ini!")
        break

    else:
        print("Pilihan tidak valid, silahkan coba lagi.")
