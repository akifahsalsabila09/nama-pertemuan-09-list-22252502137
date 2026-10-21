def rata_rata(data):
    if len(data) == 0:
        return 0
    return sum(data) / len(data)

def nilai_lulus(data, batas=60):
    hasil = []
    for x in data:
        if x >= batas:
            hasil.append(x)
    return hasil

# 1. Siapkan list nilai (minimal 10 nilai)
nilai = [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]

# 2. Proses pengolahan data
lulus = nilai_lulus(nilai)
jumlah_lulus = len(lulus)
jumlah_belum_lulus = len(nilai) - jumlah_lulus

# 3. Tampilkan hasil ringkasan statistik
print(f"Data                : {nilai}")
print(f"Banyak data         : {len(nilai)}")
print(f"Total               : {sum(nilai)}")
print(f"Rata-rata           : {rata_rata(nilai):.2f}")
print(f"Minimum             : {min(nilai)}")
print(f"Maksimum            : {max(nilai)}")
print(f"Nilai lulus         : {lulus}")
print(f"Jumlah lulus        : {jumlah_lulus}")
print(f"Jumlah belum lulus  : {jumlah_belum_lulus}")