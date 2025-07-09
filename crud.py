def catat_transaksi(data, tanggal, deskripsi, jenis, tipe, jumlah):
    transaksi = {
        'Tanggal': tanggal,
        'Deskripsi': deskripsi,
        'Jenis': jenis,
        'Tipe': tipe,
        'Jumlah': int(jumlah)
    }
    data.append(transaksi)
    print("Transaksi berhasil dicatat.")


def tampilkan_rekap(data):
    if not data:
        print("Belum ada transaksi.")
        return

    print("\n=== Rekap Transaksi ===")
    for idx, transaksi in enumerate(data):
        print(f"{idx+1}. {transaksi['Tanggal']} | {transaksi['Deskripsi']} | {transaksi['Jenis']} | {transaksi['Tipe']} | {transaksi['Jumlah']}")


def update_transaksi(data, index):
    if 0 <= index < len(data):
        print("Masukkan data baru:")
        tanggal = input("Tanggal (DD-MM-YYYY): ")
        deskripsi = input("Deskripsi: ")
        jenis = input("Jenis: ")
        tipe = input("Tipe (Pemasukkan/Pengeluaran): ")
        jumlah = input("Jumlah: ")

        data[index] = {
            'Tanggal': tanggal,
            'Deskripsi': deskripsi,
            'Jenis': jenis,
            'Tipe': tipe,
            'Jumlah': int(jumlah)
        }
        print("Transaksi berhasil diperbarui.")
    else:
        print("Nomor transaksi tidak valid.")


def hapus_transaksi(data, index):
    if 0 <= index < len(data):
        data.pop(index)
        print("Transaksi berhasil dihapus.")
    else:
        print("Nomor transaksi tidak valid.")
