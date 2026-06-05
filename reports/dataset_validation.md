# Dataset Validation

# Overview

Tahap Dataset Validation dilakukan setelah proses Data Cleaning untuk memastikan bahwa dataset yang dihasilkan memiliki kualitas yang memadai dan siap digunakan pada tahap ekstraksi landmark, feature engineering, dan pelatihan model.

Validasi dilakukan terhadap seluruh video yang telah lolos proses cleaning dengan fokus pada distribusi kelas, jumlah sampel, karakteristik video, serta potensi class imbalance.

---

# Validation Objective

Tujuan dari proses validasi dataset adalah:

* Memastikan seluruh data dapat digunakan pada tahap pemodelan.
* Memastikan jumlah sampel pada setiap kelas mencukupi.
* Mengidentifikasi potensi class imbalance.
* Memverifikasi konsistensi karakteristik video.
* Menentukan kelayakan dataset untuk proses training model.

---

# Dataset Summary

| Metric         | Value |
| -------------- | ----- |
| Total Labels   | 49    |
| Total Videos   | 5094  |
| Dataset Status | VALID |

Dataset hasil validasi terdiri dari 49 kelas gesture yang mencakup alfabet, angka, istilah perbankan, dan istilah keuangan.

---

# Class Distribution Analysis

Distribusi jumlah video pada setiap kelas dianalisis untuk memastikan tidak terdapat ketimpangan data yang signifikan.

| Metric                    | Value |
| ------------------------- | ----- |
| Minimum Samples per Class | 100   |
| Maximum Samples per Class | 154   |
| Imbalance Ratio           | 1.54  |

Visualisasi:

* validation_class_distribution.png

Hasil analisis menunjukkan bahwa seluruh kelas memiliki jumlah sampel yang relatif seimbang. Kelas dengan jumlah data paling sedikit masih memiliki 100 video, sedangkan kelas dengan jumlah data terbanyak memiliki 154 video.

Nilai imbalance ratio sebesar 1.54 menunjukkan bahwa distribusi dataset masih berada dalam rentang yang dapat diterima dan tidak memerlukan teknik penyeimbangan data tambahan seperti undersampling atau oversampling.

---

# Dataset Adequacy Analysis

Jumlah sampel yang tersedia pada setiap kelas dinilai cukup untuk proses pelatihan model berbasis sequence seperti Long Short-Term Memory (LSTM).

Dengan total 5094 video dan minimum 100 video pada setiap kelas, dataset memiliki variasi yang memadai untuk membantu model mempelajari pola gesture dari berbagai individu, kondisi pencahayaan, latar belakang, dan sudut pengambilan gambar.

---

# Video Consistency Validation

Selain distribusi kelas, dilakukan pemeriksaan terhadap karakteristik video untuk memastikan konsistensi data.

Aspek yang diperiksa meliputi:

* Format video
* Resolusi video
* Frame rate (FPS)
* Durasi video
* Jumlah frame

Pemeriksaan dilakukan untuk memastikan bahwa seluruh video memenuhi standar yang telah ditetapkan selama proses pengumpulan data.

---

# Validation Findings

Berdasarkan proses validasi, diperoleh beberapa temuan utama:

1. Dataset terdiri dari 5094 video valid.
2. Dataset mencakup 49 kelas gesture.
3. Seluruh kelas memiliki minimal 100 sampel.
4. Tidak ditemukan class imbalance yang signifikan.
5. Dataset dinyatakan layak untuk digunakan pada tahap ekstraksi landmark dan pelatihan model.

---

# Conclusion

Berdasarkan hasil Dataset Validation, dataset SignBank AI dinyatakan valid dan siap digunakan pada tahap berikutnya.

Distribusi kelas yang relatif seimbang, jumlah sampel yang memadai, serta kualitas video yang konsisten menjadi dasar bahwa dataset telah memenuhi kebutuhan untuk pengembangan model klasifikasi gesture berbasis LSTM.

Tahap selanjutnya adalah proses Landmark Extraction menggunakan MediaPipe untuk mengubah data video menjadi representasi numerik yang dapat digunakan oleh model machine learning.
