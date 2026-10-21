# Pertemuan 09 - List dan Pengolahan Data Numerik
Nama: Akifah Salsabila
NIM: 2225250137
Kelas: 3F

## Tujuan

Mengolah kumpulan data numerik menggunakan list Python, termasuk mengakses elemen berdasarkan indeks, menghitung jumlah data, dan menghitung nilai rata-rata.

## Struktur Program

Proyek ini terdiri atas folder dan file berikut:

```text
.
├── latihan/
│   └── README.md
└── praktik/
    └── analisis_nilai_mahasiswa.py
```

- **Folder `latihan/`** berisi dokumentasi atau catatan latihan mengenai konsep list Python, seperti indeks, slicing, `append()`, `insert()`, `len()`, dan `sum()`.
- **File `praktik/analisis_nilai_mahasiswa.py`** berisi program praktik untuk menyimpan data nilai mahasiswa dalam list, menampilkan data, menghitung jumlah nilai, dan menghitung rata-rata.

## Cara Menjalankan

Jalankan perintah berikut dari direktori utama proyek:

```bash
python3 praktik/analisis_nilai_mahasiswa.py
```

Pastikan Python 3 sudah terpasang dan terminal berada di direktori utama proyek.

## Test Case

| No. | Data/kondisi uji | Hasil yang diharapkan | Hasil aktual | Status |
|---|---|---|---|---|
| 1 | `[80, 90, 70]` | Jumlah data 3 dan rata-rata 80.0 | Belum dijalankan | Belum diuji |
| 2 | Mengakses indeks `0` | Nilai 80 | Belum dijalankan | Belum diuji |
| 3 | Mengakses indeks `-1` | Nilai 70 | Belum dijalankan | Belum diuji |
| 4 | List kosong `[]` | Program tidak membagi dengan nol dan menampilkan pesan bahwa data belum tersedia | Belum dijalankan | Belum diuji |

Catatan: Kolom hasil aktual harus diisi berdasarkan keluaran program setelah dijalankan. Status **Lulus** diberikan jika hasil aktual sesuai dengan hasil yang diharapkan, sedangkan **Gagal** diberikan jika hasilnya tidak sesuai.

## Refleksi

- **Hal yang dipahami:** Indeks list Python dimulai dari 0, sedangkan indeks -1 digunakan untuk mengambil elemen terakhir. List memudahkan penyimpanan dan pengolahan banyak nilai dalam satu variabel.
- **Kesalahan yang berhasil diperbaiki:** Memeriksa apakah list kosong sebelum menghitung rata-rata agar program tidak mengalami `ZeroDivisionError` ketika `len(data)` bernilai 0.

## Kesimpulan

List Python memudahkan pengelolaan kumpulan nilai secara terstruktur. Fungsi `len()` digunakan untuk menghitung banyak data, sedangkan `sum()` digunakan untuk menjumlahkan nilai. Sebelum menghitung rata-rata, pastikan list berisi data agar pembagian dapat dilakukan dengan aman.