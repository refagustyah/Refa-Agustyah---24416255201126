def laporan_bulanan(data, bulan, tahun):
    print(f"\n=== Laporan Bulanan: {bulan}-{tahun} ===")
    total_pemasukkan = 0
    total_pengeluaran = 0

    for transaksi in data:
        tgl, bln, thn = transaksi['Tanggal'].split('-')
        if int(bln) == bulan and thn == tahun:
            print(f"{transaksi['Tanggal']} | {transaksi['Deskripsi']} | {transaksi['Jenis']} | {transaksi['Tipe']} | {transaksi['Jumlah']}")
            if transaksi['Tipe'] == 'Pemasukkan':
                total_pemasukkan += int(transaksi['Jumlah'])
            else:
                total_pengeluaran += int(transaksi['Jumlah'])

    print(f"Total Pemasukkan: {total_pemasukkan}")
    print(f"Total Pengeluaran: {total_pengeluaran}")


def laporan_tahunan(data, tahun):
    print(f"\n=== Laporan Tahunan: {tahun} ===")
    total_pemasukkan = 0
    total_pengeluaran = 0

    for transaksi in data:
        tgl, bln, thn = transaksi['Tanggal'].split('-')
        if thn == tahun:
            print(f"{transaksi['Tanggal']} | {transaksi['Deskripsi']} | {transaksi['Jenis']} | {transaksi['Tipe']} | {transaksi['Jumlah']}")
            if transaksi['Tipe'] == 'Pemasukkan':
                total_pemasukkan += int(transaksi['Jumlah'])
            else:
                total_pengeluaran += int(transaksi['Jumlah'])

    print(f"Total Pemasukkan: {total_pemasukkan}")
    print(f"Total Pengeluaran: {total_pengeluaran}")
