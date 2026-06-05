# Feature Engineering

# Overview

Feature Engineering merupakan tahap transformasi data yang bertujuan mengubah data video gesture menjadi representasi numerik yang dapat diproses oleh model machine learning. Pada penelitian ini, proses feature engineering dilakukan menggunakan MediaPipe Hands untuk mengekstraksi koordinat landmark tangan serta menambahkan fitur sudut (angle feature) guna memperkaya representasi gerakan bahasa isyarat.

Output dari tahap ini berupa sequence data yang siap digunakan sebagai input model Long Short-Term Memory (LSTM).

---

# Input Data

Data masukan berasal dari dataset hasil cleaning yang terdiri dari video gesture bahasa isyarat perbankan.

| Attribute     | Value     |
| ------------- | --------- |
| Total Classes | 50        |
| Total Videos  | 5094      |
| Resolution    | 512 × 512 |
| FPS           | 30        |
| Duration      | 2–5 detik |
| Dataset Type  | Primer    |

Dataset hasil cleaning digunakan sebagai sumber utama untuk proses ekstraksi fitur.

---

# Landmark Extraction

Ekstraksi fitur dilakukan menggunakan MediaPipe Hands.

Pada setiap frame, MediaPipe mendeteksi:

* 21 landmark tangan kiri
* 21 landmark tangan kanan

Setiap landmark memiliki tiga koordinat:

* x
* y
* z

Sehingga diperoleh:

21 × 3 = 63 fitur tangan kiri

21 × 3 = 63 fitur tangan kanan

Total fitur koordinat:

63 + 63 = 126 fitur

---

# Coordinate Features

Koordinat landmark digunakan untuk merepresentasikan posisi tangan pada setiap frame.

Struktur fitur:

```text
Left Hand:
left_x_0
left_y_0
left_z_0
...
left_x_20
left_y_20
left_z_20

Right Hand:
right_x_0
right_y_0
right_z_0
...
right_x_20
right_y_20
right_z_20
```

Jumlah fitur koordinat:

126 fitur

---

# Angle Features

Selain koordinat landmark, penelitian ini menggunakan fitur sudut (angle feature) untuk menangkap hubungan geometris antar sendi jari.

Sudut dihitung menggunakan tiga titik landmark yang membentuk suatu segmen jari.

Fitur sudut digunakan untuk:

* Membantu membedakan gesture yang memiliki posisi tangan mirip.
* Menangkap informasi bentuk jari.
* Meningkatkan robustness model terhadap variasi posisi tangan.

Jumlah angle feature:

15 fitur

---

# Final Feature Representation

Total fitur pada setiap frame terdiri dari:

| Feature Type        | Total |
| ------------------- | ----- |
| Coordinate Features | 126   |
| Angle Features      | 15    |
| Total Features      | 141   |

Sehingga setiap frame direpresentasikan sebagai:

```text
141 fitur
```

---

# Sequence Normalization

Durasi video pada dataset bervariasi antara 2 hingga 5 detik sehingga jumlah frame setiap video tidak seragam.

Untuk menghasilkan input yang konsisten bagi model LSTM, seluruh sequence dinormalisasi menggunakan metode frame resampling.

Panjang sequence yang digunakan:

```text
40 frame
```

Metode ini memastikan seluruh sampel memiliki ukuran input yang sama tanpa bergantung pada durasi video asli.

---

# Output Shape

Setelah proses ekstraksi dan normalisasi sequence, setiap video direpresentasikan dalam bentuk:

```text
(40, 141)
```

Keterangan:

* 40 = jumlah frame sequence
* 141 = jumlah fitur pada setiap frame

---

# Extraction Result

Hasil proses ekstraksi fitur:

| Metric                 | Value |
| ---------------------- | ----- |
| Total Videos Processed | 5094  |
| Success Files          | 5094  |
| Failed Files           | 0     |
| Success Rate           | 100%  |

Seluruh video berhasil diekstraksi tanpa kegagalan proses.

---

# Generated Dataset

Dataset hasil ekstraksi disimpan pada:

```text
dataset_landmarks/
```

Struktur folder:

```text
dataset_landmarks/
├── A/
├── B/
├── C/
├── ...
├── ATM/
├── SALDO/
├── TRANSFER/
```

Setiap file disimpan dalam format:

```text
.npy
```

yang berisi sequence fitur dengan ukuran:

```text
(40, 141)
```

---

# Contribution to Business Questions

Tahap feature engineering berperan penting dalam menjawab pertanyaan bisnis yang telah ditetapkan.

1. Seberapa akurat SignBank AI dalam menerjemahkan bahasa isyarat perbankan menjadi teks secara real-time?

Landmark dan angle feature digunakan sebagai representasi utama gesture yang akan dipelajari model untuk menghasilkan prediksi yang akurat.

2. Bagaimana performa SignBank AI dalam mendukung komunikasi antara nasabah Tuli dan petugas bank berdasarkan hasil pengujian model?

Representasi fitur yang lebih informatif diharapkan dapat meningkatkan kemampuan model dalam mengenali gesture bahasa isyarat perbankan secara konsisten.

---

# Conclusion

Proses feature engineering berhasil mengubah data video gesture menjadi representasi numerik berbentuk sequence yang siap digunakan oleh model LSTM.

Melalui kombinasi 126 fitur koordinat landmark dan 15 angle feature, setiap video direpresentasikan sebagai sequence berukuran (40, 141). Seluruh video berhasil diproses dengan tingkat keberhasilan ekstraksi sebesar 100%, sehingga dataset siap digunakan pada tahap Exploratory Data Analysis (EDA) dan pelatihan model.
