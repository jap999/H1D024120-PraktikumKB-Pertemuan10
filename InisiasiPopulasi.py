import random
# Fungsi untuk inisialisasi populasi
def inisialisasi_populasi(jumlah_populasi, jumlah_gen):
    populasi = []
    for i in range(jumlah_populasi):
        # Membuat kromosom dengan gen biner secara acak
        kromosom = [random.randint(0, 1) for _ in range(jumlah_gen)]
        populasi.append(kromosom)
    # PERBAIKAN: return dipindah KELUAR dari loop
    # SALAH: return di dalam loop → hanya 1 individu yang dibuat
    # BENAR: return setelah loop selesai → semua jumlah_populasi individu terbuat
    # ALASAN: Jika return dalam loop, fungsi langsung return saat i=0, tidak ada iterasi selanjutnya
    return populasi

# PERBAIKAN: Wrap contoh kode dengan if __name__ == "__main__"
# ALASAN: Saat import, kode di bawah tidak perlu dijalankan, hanya fungsi yang dibutuhkan
if __name__ == "__main__":
    # Menampilkan populasi awal
    print("Populasi Awal:")
    jumlah_populasi = 10  # Jumlah individu dalam populasi
    jumlah_gen = 5  # Jumlah barang (gen) dalam kromosom
    
    populasi_awal = inisialisasi_populasi(jumlah_populasi, jumlah_gen)
    for idx, individu in enumerate(populasi_awal):
        print(f"Individu {idx+1}: {individu}")

