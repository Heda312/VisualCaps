# Data Gathering

# Dataset Collection

## Data Source

Dataset yang digunakan dalam proyek SignBank AI merupakan **data primer** yang dikumpulkan secara mandiri oleh tim pengembang. Data dikumpulkan melalui proses perekaman video gesture bahasa isyarat yang mewakili alfabet, angka, istilah perbankan, dan nominal keuangan.

Pengumpulan data dilakukan untuk memastikan ketersediaan dataset yang sesuai dengan kebutuhan proyek, karena belum tersedia dataset publik yang secara spesifik mencakup kosakata perbankan yang digunakan pada penelitian ini.

!!!
Dataset awal terdiri dari 4500 video hasil pengumpulan data primer.

Jumlah video per kelas dapat berbeda karena adanya proses penambahan data pada beberapa label untuk meningkatkan variasi gesture dan kualitas dataset.

Jumlah video per label tidak sepenuhnya seragam karena terdapat penambahan data pada beberapa label selama proses pengumpulan dataset, sehingga saat ini jumlah video berjumlah 5094.

---

# Data Collection Method

Data direkam oleh enam anggota tim dengan menggunakan perangkat kamera digital.

Setiap anggota melakukan perekaman gesture untuk seluruh label yang telah ditentukan dengan variasi kondisi lingkungan yang berbeda guna meningkatkan kemampuan generalisasi model.

Variasi yang diterapkan meliputi:

* Variasi latar belakang (background)
* Variasi pencahayaan (lighting)
* Variasi sudut pengambilan video (camera angle)
* Variasi posisi tubuh dan tangan
* Variasi kecepatan gerakan gesture

Pendekatan ini dilakukan untuk menghasilkan dataset yang lebih representatif terhadap kondisi penggunaan nyata.

---

# Dataset Specification

| Attribute                        | Value           |
| -------------------------------- | --------------- |
| Dataset Type                     | Primer          |
| Data Format                      | MP4             |
| Resolution                       | 512 × 512 pixel |
| FPS                              | 30 FPS          |
| Duration                         | 2 - 5 detik     |
| Number of Contributors           | 6 orang         |
| Videos per Label per Contributor | 15 video        |
| Total Labels                     | 50 label        |

---

# Label Categories

Dataset terdiri dari empat kelompok utama:

## Alphabet

26 label:

A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z

## Number

10 label:

0, 1, 2, 3, 4, 5, 6, 7, 8, 9

## Banking Terms

5 label:

ATM, KARTU, SALDO, TRANSFER, UANG

## Financial Terms

9 label:

10, 20, 50, 100, 500, 1000, RIBU, JUTA, MILYAR

---

# Dataset Size

Jumlah video yang dikumpulkan dihitung sebagai berikut:

Total Video = Jumlah Kontributor × Jumlah Video per Label × Jumlah Label

Total Video = 6 × 15 × 50

Total Video = 4.500 video

---

# Dataset Characteristics

Karakteristik dataset yang dikumpulkan adalah sebagai berikut:

* Gesture direkam menggunakan tangan sesuai gerakan bahasa isyarat yang digunakan.
* Setiap video hanya merepresentasikan satu label.
* Setiap video memiliki durasi antara 2 hingga 5 detik.
* Video direkam dengan kualitas resolusi yang seragam.
* Data dikumpulkan dari beberapa individu untuk mengurangi bias terhadap karakteristik tangan tertentu.
* Variasi kondisi lingkungan diterapkan untuk meningkatkan robustness model pada proses deployment.

---

# Purpose of Data Collection

Pengumpulan data dilakukan untuk membangun dataset bahasa isyarat yang dapat digunakan dalam pengembangan sistem SignBank AI. Dataset ini digunakan sebagai sumber data utama dalam proses:

1. Ekstraksi landmark tangan menggunakan MediaPipe.
2. Analisis karakteristik data.
3. Pelatihan model klasifikasi gesture berbasis LSTM.
4. Evaluasi performa model.
5. Pengembangan sistem penerjemah bahasa isyarat perbankan secara real-time.

---

# Expected Output

Output dari proses pengumpulan data adalah dataset video gesture yang siap memasuki tahap Data Assessment, Data Cleaning, dan Exploratory Data Analysis (EDA) sebelum digunakan dalam proses pelatihan model machine learning.
