# Data barang (nama, keuntungan, ukuran)
# Kasus: Toko gudang dengan kapasitas maksimal 15
barang = [
    ("Barang1", 10, 5),
    ("Barang2", 40, 4),
    ("Barang3", 30, 6),
    ("Barang4", 50, 3),
    ("Barang5", 35, 7)
]
kapasitas_tas = 15  # Kapasitas maksimum gudang

# Fungsi untuk menghitung nilai fitness (total keuntungan)
def hitung_fitness(kromosom, barang, kapasitas_tas):
    total_keuntungan = 0
    total_ukuran = 0
    for i in range(len(kromosom)):
        if kromosom[i] == 1:  # Jika barang dipilih
            total_keuntungan += barang[i][1]  # Tambahkan keuntungan
            total_ukuran += barang[i][2]  # Tambahkan ukuran
    if total_ukuran > kapasitas_tas:  # Jika melebihi kapasitas, fitness = 0
        return 0  # Penalti jika melebihi kapasitas
    else:
        return total_keuntungan  # Fitness adalah total keuntungan

# PERBAIKAN: Wrap contoh kode dengan if __name__ == "__main__"
# ALASAN: Saat import, kode di bawah tidak perlu dijalankan, hanya fungsi yang dibutuhkan
if __name__ == "__main__":
    # Definisi contoh populasi awal
    populasi_awal = [
        [1, 0, 1, 0, 1], # Contoh kromosom individu
        [0, 1, 0, 1, 0],
        [1, 1, 0, 0, 1],
        # Tambahkan lebih banyak individu sesuai kebutuhan
    ]
    # Contoh penggunaan
    fitness_populasi = [hitung_fitness(individu, barang,
    kapasitas_tas) for individu in populasi_awal]

    # Menampilkan nilai fitness
    print("\nNilai Fitness:")
    for idx, fitness in enumerate(fitness_populasi):
        print(f"Individu {idx+1}: Fitness = {fitness}")
