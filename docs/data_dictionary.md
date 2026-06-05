# Data Dictionary

# Dataset Overview

Dataset SignBank AI terdiri dari video gesture bahasa isyarat yang digunakan untuk mengenali alfabet, angka, istilah perbankan, dan nominal keuangan menggunakan pendekatan Deep Learning berbasis LSTM.

Setiap video direkam dengan kamera pada resolusi 512×512 piksel dan frame rate 30 FPS. Durasi video bervariasi antara 2 hingga 5 detik.

Video kemudian diproses menggunakan MediaPipe untuk mengekstraksi koordinat landmark tangan kanan dan tangan kiri pada setiap frame.

Output ekstraksi digunakan sebagai input sequence untuk model LSTM.

---

# Dataset Information

| Attribute                 | Value           |
| ------------------------- | --------------- |
| Data Type                 | Video Gesture   |
| Resolution                | 512 × 512 px    |
| FPS                       | 30              |
| Duration                  | 2 – 5 detik     |
| Feature Extraction        | MediaPipe Hands |
| Number of Hands           | 2 tangan        |
| Landmarks per Hand        | 21              |
| Total Landmarks           | 42              |
| Coordinates per Landmark  | x, y, z         |
| Total Coordinate Features | 126             |
| Model                     | LSTM            |

---

# Label Classes

## 1. Alphabet

26 kelas:

| Label |
| ----- |
| A     |
| B     |
| C     |
| D     |
| E     |
| F     |
| G     |
| H     |
| I     |
| J     |
| K     |
| L     |
| M     |
| N     |
| O     |
| P     |
| Q     |
| R     |
| S     |
| T     |
| U     |
| V     |
| W     |
| X     |
| Y     |
| Z     |

---

## 2. Number

10 kelas:

| Label |
| ----- |
| 0     |
| 1     |
| 2     |
| 3     |
| 4     |
| 5     |
| 6     |
| 7     |
| 8     |
| 9     |

---

## 3. Banking Terms

| Label    |
| -------- |
| ATM      |
| KARTU    |
| SALDO    |
| TRANSFER |
| UANG     |

---

## 4. Financial Terms

| Label  |
| ------ |
| 10     |
| 20     |
| 50     |
| 100    |
| 500    |
| 1000   |
| RIBU   |
| JUTA   |
| MILYAR |

---

# Total Classes

Total kelas:

26 (Alphabet)
+
10 (Number)
+
5 (Banking Terms)
+
9 (Financial Terms)

= 50 kelas

---

# Landmark Features

MediaPipe menghasilkan 21 landmark untuk setiap tangan.

## Left Hand

| Feature   |
| --------- |
| left_x_0  |
| left_y_0  |
| left_z_0  |
| ...       |
| left_x_20 |
| left_y_20 |
| left_z_20 |

Total:

21 × 3 = 63 fitur

---

## Right Hand

| Feature    |
| ---------- |
| right_x_0  |
| right_y_0  |
| right_z_0  |
| ...        |
| right_x_20 |
| right_y_20 |
| right_z_20 |

Total:

21 × 3 = 63 fitur

---

# Total Coordinate Features

63 (Left Hand)
+
63 (Right Hand)

= 126 fitur

---

# Sequence Structure

Karena model menggunakan LSTM, data disimpan dalam bentuk sequence.

Contoh:

Video 2 detik:

60 frame × 126 fitur

Video 5 detik:

150 frame × 126 fitur

Untuk menjaga ukuran input konsisten, seluruh sequence akan dinormalisasi menjadi panjang tetap menggunakan padding atau frame sampling.

Contoh bentuk data:

(X, T, F)

Dimana:

* X = jumlah sampel
* T = jumlah frame sequence
* F = jumlah fitur (126)

Contoh:

(5000, 60, 126)

artinya:

* 5000 sampel video
* 60 frame per video
* 126 fitur per frame

---

# Target Variable

| Feature  | Type    | Description                   |
| -------- | ------- | ----------------------------- |
| label    | string  | Kelas gesture yang diprediksi |
| class_id | integer | Hasil encoding label          |

---

# Final Dataset

Dataset akhir yang digunakan pada proses training terdiri dari:

* X_train.npy
* X_val.npy
* X_test.npy
* y_train.npy
* y_val.npy
* y_test.npy

Seluruh data telah melalui proses validasi, cleaning, normalisasi, dan ekstraksi landmark sebelum digunakan pada tahap pelatihan model.
