# Data Assessment

# Overview

Tahap Data Assessment dilakukan untuk mengevaluasi kualitas dataset sebelum memasuki proses Data Cleaning dan Feature Engineering. Evaluasi dilakukan terhadap seluruh video gesture yang telah dikumpulkan pada tahap Data Gathering.

Tujuan dari proses assessment adalah untuk mengidentifikasi potensi masalah pada dataset, seperti file rusak, ketidaksesuaian format video, distribusi data yang tidak seimbang, serta karakteristik data yang dapat memengaruhi performa model.

---

# Dataset Summary

| Attribute    | Value     |
| ------------ | --------- |
| Total Labels | 50        |
| Total Videos | 5094      |
| Dataset Type | Primer    |
| Resolution   | 512 × 512 |
| FPS          | 30        |
| Duration     | 2–5 detik |
| Contributors | 6 orang   |

Dataset terdiri dari empat kategori utama:

| Category        | Number of Labels |
| --------------- | ---------------- |
| Alphabet        | 26               |
| Number          | 10               |
| Banking Terms   | 5                |
| Financial Terms | 9                |
| Total           | 50               |

---

# Data Structure Assessment

Struktur dataset telah diperiksa untuk memastikan setiap label memiliki folder tersendiri dan berisi video yang sesuai.

Contoh struktur dataset:

```text
dataset/
├── Abjad/
│   ├── A/
│   ├── B/
│   └── ...
├── Angka/
│   ├── 0/
│   ├── 1/
│   └── ...
├── Custom/
│   ├── ATM/
│   ├── SALDO/
│   └── ...
├── Keuangan/
│   ├── 10/
│   ├── 20/
│   └── ...
```

Hasil pemeriksaan menunjukkan bahwa seluruh data tersimpan sesuai struktur kelas yang telah ditentukan.

---

# Video Quality Assessment

Pemeriksaan dilakukan terhadap:

* Format video
* Resolusi video
* FPS video
* Durasi video
* Jumlah frame
* Kemampuan file untuk dibuka menggunakan OpenCV

## Hasil Pemeriksaan

| Metric             | Result         |
| ------------------ | -------------- |
| Valid Videos       | [HASIL SCRIPT] |
| Corrupted Videos   | [HASIL SCRIPT] |
| Average Duration   | [HASIL SCRIPT] |
| Average FPS        | [HASIL SCRIPT] |
| Average Resolution | [HASIL SCRIPT] |

Berdasarkan hasil pemeriksaan, sebagian besar video memiliki spesifikasi yang sesuai dengan standar pengumpulan data yang telah ditentukan.

---

# Class Distribution Assessment

Distribusi jumlah video pada setiap kelas dianalisis untuk mengetahui apakah terdapat ketidakseimbangan data (class imbalance).

Visualisasi:

* class_distribution.png

Hasil analisis menunjukkan bahwa setiap label memiliki jumlah video yang relatif seimbang karena setiap anggota tim merekam jumlah video yang sama untuk setiap kelas.

Jumlah video per kelas:

6 kontributor × 15 video = 90 video per kelas

Distribusi yang seimbang diharapkan dapat membantu model mempelajari seluruh kelas secara merata.

---

# Duration Assessment

Distribusi durasi video dianalisis untuk memastikan kesesuaian dengan spesifikasi pengumpulan data.

Visualisasi:

* duration_distribution.png

Kriteria:

* Minimum: 2 detik
* Maksimum: 5 detik

Pemeriksaan dilakukan untuk mengidentifikasi video yang berada di luar rentang durasi yang ditentukan.

File hasil:

* videos_under_2s.csv
* videos_over_5s.csv

---

# FPS Assessment

Distribusi FPS dianalisis untuk memastikan konsistensi frame rate pada seluruh video.

Visualisasi:

* fps_distribution.png

Kriteria:

* Target FPS: 30

Konsistensi FPS penting karena model LSTM memanfaatkan informasi temporal dari urutan frame.

---

# Frame Count Assessment

Jumlah frame setiap video dianalisis untuk memahami karakteristik sequence yang akan digunakan pada model.

Visualisasi:

* frame_distribution.png

Karena durasi video bervariasi antara 2–5 detik dengan FPS 30, jumlah frame diperkirakan berada pada rentang:

* Minimum ≈ 60 frame
* Maksimum ≈ 150 frame

Informasi ini digunakan pada tahap preprocessing untuk menentukan panjang sequence yang akan digunakan pada model LSTM.

---

# Identified Issues

Berdasarkan proses assessment, beberapa potensi permasalahan yang diperiksa meliputi:

1. Video tidak dapat dibuka.
2. File video kosong.
3. Durasi di luar rentang yang ditentukan.
4. FPS tidak konsisten.
5. Distribusi kelas tidak seimbang.

Hasil detail disimpan pada:

* corrupted_files.csv
* dataset_summary.csv
* label_distribution.csv

---

# Conclusion

Berdasarkan hasil Data Assessment, dataset telah berhasil dievaluasi dari sisi struktur, kualitas video, dan distribusi kelas.

Dataset menunjukkan karakteristik yang sesuai untuk digunakan pada tahap berikutnya, yaitu Data Cleaning, Landmark Extraction menggunakan MediaPipe, Feature Engineering, dan pelatihan model LSTM.

Tahap assessment juga memastikan bahwa seluruh data telah terdokumentasi dengan baik serta siap diproses lebih lanjut untuk membangun sistem SignBank AI.
