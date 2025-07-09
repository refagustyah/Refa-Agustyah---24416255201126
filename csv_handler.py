import csv

def baca_data(nama_file):
    try:
        with open(nama_file, 'r', newline='') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        return []


def tulis_data(nama_file, data):
    with open(nama_file, 'w', newline='') as file:
        fieldnames = ['Tanggal', 'Deskripsi', 'Jenis', 'Tipe', 'Jumlah']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for item in data:
            writer.writerow({
                'Tanggal': item['Tanggal'],
                'Deskripsi': item['Deskripsi'],
                'Jenis': item['Jenis'],
                'Tipe': item['Tipe'],
                'Jumlah': item['Jumlah']
            })
